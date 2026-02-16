import argparse
import ast
import re
import sys
import warnings
import yaml

from pathlib import Path
from typing import Any, Optional, Sequence

from docstring_parser import Docstring, numpydoc, parse

# parse_docstring = parse
parse_docstring = numpydoc.parse  # Ensure numpydoc parser

####################
# Config Constants #
####################

_BASE_DIR = Path(__file__).resolve().parent

DOCS_TRACKER = _BASE_DIR / "docs_status.yaml"
PARSE_DIR = _BASE_DIR / "synology_api"
API_LIST_FILE = _BASE_DIR / "documentation" / "docs" / "apis" / "readme.md"
DOCS_DIR = _BASE_DIR / "documentation" / "docs" / "apis" / "classes"

EXCLUDED_FILES = {'__init__.py', 'auth.py', 'base_api.py',
                  'error_codes.py', 'exceptions.py', 'utils.py'}

####################
# String Constants #
####################

META_TAG = '---\n'
SEPARATOR = '\n\n\n---\n\n\n'
NEWLINE = '  \n'
AUTO_GEN_TAG = '\n<!-- ' + '-'*44 + ' -->\n'
AUTO_GEN_MESSAGE = '<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->'
AUTO_GEN_DISCLAIMER = AUTO_GEN_TAG + AUTO_GEN_MESSAGE + AUTO_GEN_TAG + NEWLINE

##################
# RegEx Patterns #
##################

# Match admonitions, level in group 1 and message in group 2
ADMONITIONS = [
    {'pattern': r'(Note:)(.*)', 'level': 'note'},
    {'pattern': r'(Info:)(.*)', 'level': 'info'},
    {'pattern': r'(Tip:)(.*)', 'level': 'tip'},
    {'pattern': r'(Warning:)(.*)', 'level': 'warning'},
    {'pattern': r'(Danger:)(.*)', 'level': 'danger'},
]

EXAMPLE_RETURN_PATTERN = r'(?s)```.+```'

#############
#   Utils   #
#############

def write(path: Path, content: str):
    with open(path, 'w', encoding="utf-8") as f:
        print('Writing into:', path)
        f.write(content)

def get_docs_status():
    with open(DOCS_TRACKER, 'r') as stream:
        return yaml.safe_load(stream)

class WarningCatcher:
    def __init__(self):
        self.warnings = []

    def __call__(self, message, category, filename, lineno, file=None, line=None):
        msg = warnings.formatwarning(message, category, filename, lineno, line)
        self.warnings.append(msg)

    def has_warnings(self):
        return bool(self.warnings)

    def print_warnings(self):
        for w in self.warnings:
            print(w, end='')

####################
# Formatting utils #
####################

def __stylize(text: str, styles: list[str]) -> str:
    style_map = {'code': '`', 'bold': '**', 'italic': '_', 'underline': '___'}
    content = ''
    for style_str in styles:
        if style_str not in style_map:
            warnings.warn(f'Unknown style: {style_str}', UserWarning)
        content += style_map.get(style_str, '')
    content += text
    for style_str in reversed(styles):
        content += style_map.get(style_str, '')
    return content

def header(level: str, text: str, styles: list[str] = []) -> str:
    """Generate header element with styles"""
    header_levels = {'h1': '#', 'h2': '##', 'h3': '###', 'h4': '####'}
    if level not in header_levels:
        warnings.warn(f'Unknown header level: {level}', UserWarning)
    return header_levels.get(level, '') + ' ' + __stylize(text, styles) + '\n'

def text(text: str, styles: list[str] = [], newline: bool = False) -> str:
    """Generate text element with styles"""
    return __stylize(text, styles) + (NEWLINE if newline else ' ')

def link(text: str, url: str, fullstop: bool = False, newline: bool = False) -> str:
    """Generate link element"""
    return f' [{text}]({url})' + ('.' if fullstop else ' ') + (NEWLINE if newline else '')

def div(content: str, spacing: str = '', side: str = '', size: str = '') -> str:
    """Generate div element"""
    return f'<div class="{spacing}-{side}--{size}">\n\n{content}</div>\n'

def details(summary: str, content: str, newline: bool = False) -> str:
    """Generate details element"""
    details = f'<details>\n<summary>{summary}</summary>\n'
    details += f'\n{content}\n</details>'
    return details + (NEWLINE if newline else '')

def list_item(text: str, styles: list[str] = []) -> str:
    """Generate list element"""
    return f'- {__stylize(text, styles)}{NEWLINE}'

def admonition(level: str, text: str) -> str:
    """Generate admonition"""
    return f':::{level}\n \n{text}\n \n:::\n'

def insert_admonitions(content: str) -> str:
    for adm in ADMONITIONS:
        content = re.sub(adm['pattern'], lambda match: admonition(
            adm['level'], match.group(2)), content)
    return content

def dedup_newlines(text: str) -> str:
    return re.sub(r'\n{2}', '  \n', text)

def validate_str(context: str, strs: list[str | Any]):
    for current in strs:
        if not isinstance(current, str):
            warnings.warn(
                f'[{context}] Invalid string: {current}', UserWarning)

def multi_class_disclaimer(main_class: str, additional_classes: Sequence[str]) -> str:
    """Return tip informing about all classes documented on the page"""
    content = f'This page contains documentation for the `{main_class}` class and its subclasses:  \n'
    for class_name in additional_classes:
        content += list_item(link(class_name, f'#{class_name.lower()}'))
    return admonition('tip', content)

def status_disclaimer(status: str) -> str:
    """Return admonition disclaimer based on API status"""
    if status == 'partial':
        return admonition('warning', 'This API is partially documented or under construction.')
    elif status == 'not_started':
        return admonition('warning', 'This API is not documented yet.')
    return ''

def format_method_api(method_name: str, api_name: Optional[str]) -> str:
    section = ''
    if api_name:
        section = header('h4', 'Internal API')
        section += div(text(api_name, ['code'], newline=True), 'padding', 'left', 'md')
    else:
        print(f'Method {method_name} seems to not be directly calling any internal API, this is expected for utility methods that use other calls in the class. You can ignore this message if this is the case.')
    return section + NEWLINE

def format_parameters(docstring: Docstring, method: Optional[str] = None) -> str:
    parameters = ''
    if docstring.params:
        parameters = header('h4' if method else 'h3', 'Parameters')
        parameters_body = ''
        for param in docstring.params:
            # no need to validate str if we are parsing class params
            if method:
                validate_str(method + ' - params',
                             [param.arg_name, param.type_name, param.description])
            parameters_body += text(param.arg_name or '', ['bold', 'italic'])
            parameters_body += text(param.type_name or '',
                                    ['code'], newline=True)
            # parameters_body += text(dedup_newlines(
            #     param.description or ''), newline=True)
            parameters_body += text(param.description or '', newline=True)
            parameters_body += NEWLINE
        parameters += div(content=parameters_body,
                          spacing='padding', side='left', size='md')
    return parameters + NEWLINE

#################
#    Parsing    #
#################

def parse_and_validate_args() -> tuple[list[str], bool, bool, bool]:
    """
    Create the CLI parser, parse argv, validate combinations, and resolve the list of files to parse.

    Returns:
        (files, parse_api_list, parse_docs)

        files: list[str]
            Filenames (not full paths) to parse.
        parse_api_list: bool
            Whether to generate the Supported APIs page.
        parse_docs: bool
            Whether to generate per-class markdown docs.
        exit_on_warning: bool
            Whether to sys.exit(1) on warnings.
    """

    parser = argparse.ArgumentParser(
        description=("This script parses docstrings from the wrapper source files and generates markdown files for docusaurus.")
    )

    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Parse all non-excluded files",
    )
    parser.add_argument(
        "-f", "--file",
        type=str,
        action="extend",
        nargs="+",
        help="Parse specified files. This overrides the excluded files.",
    )
    parser.add_argument(
        "-l", "--api-list",
        action="store_true",
        help="Parses APIs used by the class and generates MD for Supported APIs page.",
    )
    parser.add_argument(
        "-e", "--excluded",
        action="store_true",
        help="Show a list of the excluded files to parse.",
    )
    parser.add_argument(
        "--exit-on-warning",
        action="store_true",
        help="Exit if a warning is encountered.",
    )

    # Called with no arguments
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Called with --excluded/-e
    if args.excluded:
        print("Excluded files:")
        for name in sorted(EXCLUDED_FILES):
            print(name)
        sys.exit(1)

    if args.all or args.api_list:
        # Called with -a or -l  ->  list all non-excluded files
        files = [p.name for p in PARSE_DIR.iterdir() if p.is_file() and p.name not in EXCLUDED_FILES]
    elif args.file:
        # Called with -f [FILE1, ...]
        files = args.file
    else:
        parser.error("At least one of --all/-a, --api-list/-l or --file/-f FILE1 [FILE2 ...] must be provided.")

    return files, bool(args.api_list), bool(args.all or args.file), args.exit_on_warning

def extract_file_info(file_path: Path, verbose: bool = False) -> dict[str, dict[str, Any]]:
    """
    AST-parse a Python file and extract class/method docstrings + inferred API names.

    Docstrings are returned as `docstring_parser.Docstring` objects (or None if absent/unparseable).

    Returns:
    {
        'docstring': < file-level Docstring >
        'classes': {
            'Class1': {
                'index': < integer index (position in file) >
                'docstring': < class-level Docstring >,
                'methods': {
                    'method1': {
                        'docstring':< method-level Docstring >,,
                        'api_name': str|None,  # method api_name if found, else class-level _API_NAME, else None
                    },
                    ...
                },
                'api_names': < set of all above methods' `api_name`s >
            },
            ...
        },
      ...
    }
    """

    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    def _is_private(name: str) -> bool:
        return name.startswith("_")

    def _parse_docstring(text: Optional[str]) -> Optional[Docstring]:
        if not text:
            return None
        try:
            return parse_docstring(text)
        except Exception:
            return None

    def _get_docstring(node: ast.Module | ast.FunctionDef | ast.ClassDef) -> Optional[Docstring]:
        raw = ast.get_docstring(node, clean=True)
        return _parse_docstring(raw)

    def _token_from_name_or_attr(expr: ast.AST) -> Optional[str]:
        # self.foo -> {FOO}
        if isinstance(expr, ast.Attribute) and isinstance(expr.value, ast.Name) and expr.value.id == "self":
            return "{" + expr.attr.upper() + "}"
        # foo -> {FOO}
        if isinstance(expr, ast.Name):
            return "{" + expr.id.upper() + "}"
        return None

    def _resolve_string_expr(expr: ast.AST) -> Optional[str]:
        """
        String resolution:
          - "literal" -> "literal"
          - f"pre{self.x}post" -> "pre{X}post"
          - "pre" + self.x + "post" -> "pre{X}post"
        Returns None if not resolvable.
        """
        if isinstance(expr, ast.Constant) and isinstance(expr.value, str):
            return expr.value

        if isinstance(expr, ast.JoinedStr):
            parts: list[str] = []
            for v in expr.values:
                if isinstance(v, ast.Constant) and isinstance(v.value, str):
                    parts.append(v.value)
                elif isinstance(v, ast.FormattedValue):
                    tok = _token_from_name_or_attr(v.value)
                    if tok is None:
                        return None
                    parts.append(tok)
                else:
                    return None
            return "".join(parts)

        if isinstance(expr, ast.BinOp) and isinstance(expr.op, ast.Add):
            left = _resolve_string_expr(expr.left)
            right = _resolve_string_expr(expr.right)
            if left is not None and right is not None:
                return left + right

            # best-effort tokenization if one side is resolvable and the other is name/attr-like
            if left is not None:
                tok = _token_from_name_or_attr(expr.right)
                return (left + tok) if tok is not None else None
            if right is not None:
                tok = _token_from_name_or_attr(expr.left)
                return (tok + right) if tok is not None else None

        return None

    def _extract_class_api_name(class_node: ast.ClassDef) -> Optional[str]:
        """
        Detect `_API_NAME = "..."` or `_api_name = "..."` in the class body.
        Only accepts literal string values.
        """
        for stmt in class_node.body:
            if not isinstance(stmt, ast.Assign) or len(stmt.targets) != 1:
                continue
            tgt = stmt.targets[0]
            if not isinstance(tgt, ast.Name):
                continue
            if tgt.id not in ("_API_NAME", "_api_name"):
                continue

            if isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str):
                return stmt.value.value

        return None

    def _extract_method_api_name(fn_node: ast.AST, parent_api_name: Optional[str] = None) -> Optional[str]:
        """
        Find assignments to local variable `api_name = <string expr>` inside the method.
        Returns the last resolvable assignment found.
        """
        last: Optional[str] = None

        for node in ast.walk(fn_node):
            if isinstance(node, ast.Assign):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name) and tgt.id == "api_name":
                        resolved = _resolve_string_expr(node.value)
                        if resolved is not None:
                            last = resolved

            elif isinstance(node, ast.AnnAssign):
                if (
                    isinstance(node.target, ast.Name)
                    and node.target.id == "api_name"
                    and node.value is not None
                ):
                    resolved = _resolve_string_expr(node.value)
                    if resolved is not None:
                        last = resolved

        return last or parent_api_name

    # ---- parse file ----

    vprint(f"Parsing file `{file_path.name}` ...")

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

        try:
            tree = ast.parse(source, filename=file_path)
        except SyntaxError as e:
            raise SyntaxError(f"Failed to parse {file_path}") from e

    file_info: dict[str, Any] = {'classes': {}}

    # File's dosctring
    file_info['docstring'] = _get_docstring(tree)

    # Iterate over classes
    cls_position_index = 0
    for cls_node in tree.body:
        if not isinstance(cls_node, ast.ClassDef) or _is_private(cls_node.name):
            continue

        vprint(f"    Parsing class `{cls_node.name}` ...")

        cls_name = cls_node.name
        cls_doc = _get_docstring(cls_node) # Class-level docstring
        cls_api = _extract_class_api_name(cls_node) # Class-level attribute `_API_NAME = ...` or `_api_name = ...`

        vprint(f"        _API_NAME: `{cls_api}`")

        methods: dict[str, dict[str, Any]] = {}

        # Iterate over methods
        for mth_node in cls_node.body:
            if not isinstance(mth_node, ast.FunctionDef) or _is_private(mth_node.name):
                continue

            mth_name = mth_node.name
            vprint(f"        Parsing method `{mth_name}` ...")

            # Method-level info
            methods[mth_node.name] = {
                "docstring": _get_docstring(mth_node),
                "internal_api": _extract_method_api_name(mth_node, parent_api_name=cls_api),
            }

            vprint(f"            internal_api: `{methods[mth_node.name]["internal_api"]}`")

        # Class-level info
        file_info['classes'][cls_name] = {
            "index": cls_position_index,
            "docstring": cls_doc,
            "api_names": {mth_info["internal_api"] for mth_info in methods.values() if mth_info["internal_api"]},
            "methods": methods,
        }

        cls_position_index += 1

    return file_info

def get_docstring_example_return(docstring: Docstring) -> str | None:
    example = [meta.description for meta in docstring.meta if meta.args == ['examples']]
    if len(example) != 1:
        return None
    code_block_match = re.match(EXAMPLE_RETURN_PATTERN, example[0])
    if code_block_match:
        return code_block_match.group(0)
    return None

###################
# Docs generation #
###################

def gen_supported_apis(supported_apis: dict[str, dict]) -> str:
    content = META_TAG
    content += 'sidebar_position: 1\n'
    content +=f'title: Supported APIs\n'
    content += META_TAG
    content += AUTO_GEN_DISCLAIMER
    content += header('h1', 'Supported APIs')
    content += text("At the moment there are quite a few APIs implemented. They could be "
                    "totally or partically implemented, for specific documentation about "
                    "an API in particular, please see ")
    content += link('APIs', './category/api-classes', fullstop=True, newline=True)

    for class_name in sorted(supported_apis.keys()):
        file_name, api_set = supported_apis[class_name]

        if not api_set:
            continue

        content += header("h3", link(class_name, f'./apis/classes/{file_name.replace(".py", "")}'))

        for api_name in sorted(api_set):
            content += list_item(api_name, ["code"])

        content += NEWLINE

    return content

def gen_doc_metadata(class_name: str) -> tuple[str, str]:
    """Generate front matter header"""
    docs_status = ""
    display_order = ""
    for i, api in enumerate(get_docs_status()):
        key = (list(api.keys())[0])
        if key == class_name:
            display_order = 1 if class_name == 'BaseApi' else i + 2
            docs_status = api[key]['status']
    status_indicator = '✅' if docs_status == 'finished' else '🚧'

    content = META_TAG
    content += f'sidebar_position: {display_order}\n'
    content += f'title: {status_indicator} {class_name}\n'
    content += META_TAG
    content += AUTO_GEN_DISCLAIMER

    return (content, docs_status)

def gen_doc_header(class_name: str, docstring: Docstring, class_index: int, additional_classes: Sequence[str]) -> str:
    content = ''
    docs_status = ''

    if class_index == 0:
        content, docs_status = gen_doc_metadata(class_name)

        # File contains more than one class: disclaimer when parsing the first one
        if additional_classes:
            content += multi_class_disclaimer(class_name, additional_classes)

    content += header('h1' if class_index == 0 else 'h2', class_name)
    content += status_disclaimer(docs_status)
    content += header('h2', 'Overview')

    docstring_content = text(docstring.short_description or '', newline=True)
    docstring_content += NEWLINE
    docstring_content += text(docstring.long_description or '', newline=True)

    docstring_content = docstring_content.replace(
        'Supported methods:', header('h3', 'Supported methods'))
    docstring_content = docstring_content.replace(
        'Getters', text('Getters', ['bold']))
    docstring_content = docstring_content.replace(
        'Setters', text('Setters', ['bold']))
    docstring_content = docstring_content.replace(
        'Actions', text('Actions', ['bold']))

    if docstring.params:
        docstring_content += NEWLINE + \
            format_parameters(docstring=docstring, method=None)

    content += docstring_content + NEWLINE

    return content

def gen_doc_method(name: str, docstring: Docstring, api_name: Optional[str]) -> str:
    content = header('h3', name, ['code'])

    if not docstring:
        return content + SEPARATOR

    description = text(docstring.short_description or '', newline=True)
    # In some cases, the whole docstring text will be parsed in the long_description.
    # Avoid appending it in that case.
    if isinstance(docstring.long_description, str) and docstring.long_description.find('Parameters') != -1:
        print(docstring.params)
        print('========>', docstring.long_description)
        warnings.warn(
            f'[{name}] failed to parse docstrings. Make sure the format is correct. Check guidelines if needed.', UserWarning)
    else:
        description += text(docstring.long_description or '', newline=True)

    description = dedup_newlines(description)

    internal_api = format_method_api(name, api_name)

    parameters = format_parameters(docstring, method=name)

    returns = '\n'
    if docstring.returns:
        validate_str(name + ' - returns',
                     [docstring.returns.type_name, docstring.returns.description])
        returns = header('h4', 'Returns')
        returns_body = text(docstring.returns.type_name or '', [
                            'code'], newline=True)
        # returns_body += text(dedup_newlines(
        #     docstring.returns.description or ''), newline=True)
        returns_body += text(docstring.returns.description or '', newline=True)
        returns += div(content=returns_body, spacing='padding',
                       side='left', size='md')
        returns += NEWLINE

    example_return = ''
    example_match = get_docstring_example_return(docstring)
    if example_match:
        example_return += header('h4', 'Example return')
        example_return += details(summary='Click to expand', content=example_match, newline=False)

    content += description
    content += internal_api
    content += parameters
    content += returns
    content += example_return
    content += SEPARATOR
    content = insert_admonitions(content)

    return content

################
# Main routine #
################

def main():
    files, parse_api_list, parse_docs, exit_on_warning = parse_and_validate_args()

    # Setup warning catcher
    warning_catcher = WarningCatcher()
    warnings.showwarning = warning_catcher

    files_info = {}
    supported_apis = {}

    for file_name in files:
        file_info = extract_file_info(PARSE_DIR / file_name, verbose=False)

        supported_apis.update({
            class_name: (file_name, class_info['api_names']) for class_name, class_info in file_info['classes'].items()
        })

        if parse_docs:
            doc_content = ''

            # Sort classes by class index (= position in the file)
            # [python < 3.7 safety, where dict does not preserve insertion order]
            sorted_class_items = sorted(file_info['classes'].items(), key=lambda keyval: keyval[1]['index'])
            for class_name, class_info in sorted_class_items:
                doc_content += gen_doc_header(
                    class_name,
                    class_info['docstring'],
                    class_info['index'],
                    tuple(c_name for c_name, _ in sorted_class_items[1:])
                )

                if class_info['methods']:
                    doc_content += header('h2', 'Methods')

                    for method_name, method_info in class_info['methods'].items():
                        doc_content += gen_doc_method(
                            method_name,
                            method_info['docstring'],
                            method_info['internal_api']
                        )

            write(DOCS_DIR / file_name.replace('.py', '.md'), doc_content)
            print('='*20)

        files_info[file_name] = file_info

    if parse_api_list:
        content = gen_supported_apis(supported_apis)
        write(API_LIST_FILE, content)

    if exit_on_warning and warning_catcher.has_warnings():
        sys.exit(1)

if __name__ == "__main__":
    main()
