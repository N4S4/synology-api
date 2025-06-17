import argparse
import re
import sys
import warnings
import yaml
from os import listdir
from os.path import isfile, join
from docstring_extractor import get_docstrings

####################
# Config Constants #
####################
DOCS_TRACKER = './docs_status.yaml'
PARSE_DIR = './synology_api'
API_LIST_FILE='./documentation/docs/apis/readme.md'
DOCS_DIR = './documentation/docs/apis/classes/'
EXCLUDED_FILES = {'__init__.py', 'auth.py', 'base_api.py', 'error_codes.py', 'exceptions.py', 'utils.py'}

####################
# String Constants #
####################
META_TAG = '---\n'
SEPARATOR = '\n\n\n---\n\n\n'
NEWLINE = '  \n'
AUTO_GEN_TAG = '\n<!-- ' + '-'*44 + ' -->\n'
AUTO_GEN_MESSAGE = '<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->'
AUTO_GEN_DISCLAIMER= AUTO_GEN_TAG + AUTO_GEN_MESSAGE + AUTO_GEN_TAG + NEWLINE

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

# Match example return block, header in group 1 and content in group 2
EXAMPLE_RETURN_PATTERN = r'(?s)(Example return\n-.*)(```.*```)'

# Match API name in string, API name in group 1
CLASS_API_NAME_PATTERN = r'api_name\s*=\s*f?[\'"](.*)[\'"]'

# Match first API name after provided method name, API name in group 1
def METHOD_API_NAME_PATTERN(method_name: str) -> str:
    return rf"(?s)def {method_name}\(.*?api_name\s*=\s*f?['\"]([^'\"]+)"

# Match concatenated string in API name, prefix in group 1, concatenation in group 2, suffix in group 3
# Applies for 'prefix' + 'concatenation' + 'suffix'
API_NAME_CONCAT_PATTERN = r'(.*)([\'"]\s*\+.*\+\s*[\'"])(.*)'

# Match concatenated f-string in API name, prefix in group 1, concatenation in group 2, suffix in group 3
# Applies for f'prefix{concatenation}suffix'
API_NAME_CONCAT_PATTERN_FSTR = r'(.*)(\{.*\})(.*)'

####################
# Style Generators #
###################
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
    return f' [{text}]({url})'+ ('.' if fullstop else ' ') + (NEWLINE if newline else '')

def div(content: str, spacing: str = '', side: str = '', size: str = '') -> str:
    """Generate div element"""
    return f'<div class="{spacing}-{side}--{size}">\n{content}\n</div>\n'

def details(summary: str, content: str) -> str:
    """Generate details element"""
    details = f'<details>\n<summary>{summary}</summary>'
    details += f'\n{content}\n</details>\n'
    return details

def list_item(text: str, styles: list[str] = []) -> str:
    """Generate list element"""
    return f'- {__stylize(text, styles)}{NEWLINE}'

def metadata(class_name: str) -> tuple[str, str]:
    """Generate front matter header"""
    docs_status=""
    display_order=""
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

def admonition(level: str, text: str) -> str:
    """Generate admonition"""
    return f':::{level}\n \n{text}\n \n:::\n'

def status_disclaimer(status: str) -> str:
    """Return admonition disclaimer based on API status"""
    if status == 'partial':
        return admonition('warning', 'This API is partially documented or under construction.')
    elif status == 'not_started':
        return admonition('warning', 'This API is not documented yet.')
    return ''

def multi_class_disclaimer(classes: list[str]) -> str:
    """Return tip informing about all classes documented on the page"""
    content = f'This page contains documentation for the `{classes[0]}` class and its subclasses:  \n'
    for i, class_name in enumerate(classes[1:], start=1):
        content += list_item(link(class_name, f'#{class_name.lower()}'))
    return admonition('tip', content)

def dedup_newlines(text: str) -> str:
    return re.sub(r'\n{2}', '  \n', text)




def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='This script parses docstrings from the wrapper source files and generates markdown files for docusaurus.'
    )
    
    parser.add_argument('-a', '--all',
                        action='store_true',
                        help='Parse all non-excluded files')
    parser.add_argument('-f', '--file',
                        type=str,
                        action='extend',
                        nargs="+",
                        help='Parse specified files. This overrides the excluded files.')  
    parser.add_argument('-l', '--api-list',
                        action='store_true',
                        help='Parses APIs used by the class and generates MD for Supported APIs page.')
    parser.add_argument('-e', '--excluded',
                        action='store_true',
                        help='Show a list of the excluded files to parse.')
    
    return parser

def get_files_to_parse() -> list[str]:
    files = listdir(PARSE_DIR)
    return [file for file in files if isfile(join(PARSE_DIR, file)) and file not in EXCLUDED_FILES]

def validate_args(parser: argparse.ArgumentParser) -> tuple[list[str], bool]:
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
    if args.excluded:
        print('Excluded files:')
        for file in EXCLUDED_FILES:
            print(file)
        sys.exit(1)

    if args.all or args.api_list:
        files = get_files_to_parse()
    elif args.file:
        files = args.file

    return (files, args.api_list, args.all or args.file)

def validate_str(context: str, strs: list[str]):
    for current in strs:
        if not isinstance(current, str):
            warnings.warn(f'[{context}] Invalid string: {current}', UserWarning)

def get_docs_status():
    with open (DOCS_TRACKER, 'r') as stream:
        return yaml.safe_load(stream)

def is_private(signature: str) -> bool:
    return signature.startswith('_')

def insert_admonitions(content: str) -> str:
    for adm in ADMONITIONS:
        content = re.sub(adm['pattern'], lambda match: admonition(adm['level'], match.group(2)), content)
    return content

def gen_supported_apis() -> str:
    content = META_TAG
    content += f'sidebar_position: 1\n'
    content += f'title: Supported APIs\n'
    content += META_TAG
    content += AUTO_GEN_DISCLAIMER
    content += header('h1', 'Supported APIs')
    content += text('At the moment there are quite a few APIs implemented. They could be totally or partically implemented, for specific documentation about an API in particular, please see')
    content += link('APIs', './category/api-classes', fullstop=True, newline=True)

    return content

def check_concatenation(api_name: str) -> str:
    match_p1 = re.search(API_NAME_CONCAT_PATTERN, api_name)
    match_p2 = re.search(API_NAME_CONCAT_PATTERN_FSTR, api_name)
    match_concat = match_p1 or match_p2

    if match_concat:
        concatenation = match_concat.group(2).replace('self.', '')
        concatenation = concatenation.replace('\'', '')
        concatenation = concatenation.replace('"', '')
        concatenation = concatenation.replace('+', '')
        concatenation = concatenation.strip()
        concatenation = concatenation.upper()
        api_name = match_concat.group(1) + '{' + concatenation + '}' + match_concat.group(3)

    return api_name

def parse_class_apis(class_name: str, file_content: str, file_path: str) -> str:
    matches = re.findall(CLASS_API_NAME_PATTERN, file_content)
    section = header('h3', link(class_name, f'./apis/classes/{file_path.replace(".py", "")}'))
    for api_name in matches:
        api_name = check_concatenation(api_name)

        if section.find(api_name) == -1: # Don't add duplicates
            section += list_item(api_name, ['code'])
    return section + NEWLINE

def parse_method_api(method_name: str, file_content: str) -> str:
    match = re.search(METHOD_API_NAME_PATTERN(method_name), file_content)
    section = ''
    if match: 
        api_name = check_concatenation(match.group(1))
        section = header('h4', 'Internal API')
        section += div(text(api_name, ['code']), 'padding', 'left', 'md')
    else:
        warnings.warn(f'Method {method_name} seems to not be directly calling any internal API, this is expected for utility methods that use other calls in the class.', UserWarning)
    return section + NEWLINE

def gen_header(class_name: str, docstring: str, classes: list[str]) -> str:
    content = ''
    docs_status = ''

    if class_name == classes[0]:
        content, docs_status = metadata(class_name)
        if len(classes) > 1:
            content += multi_class_disclaimer(classes)

    content += header('h1', class_name) if class_name == classes[0] else header('h2', class_name)
    content += status_disclaimer(docs_status)
    content += header('h2', 'Overview')

    docstring = docstring.replace('Supported methods:', header('h3', 'Supported methods'))
    docstring = docstring.replace('Getters', text('Getters', ['bold']))
    docstring = docstring.replace('Setters', text('Setters', ['bold']))
    docstring = docstring.replace('Actions', text('Actions', ['bold']))

    content += docstring + '\n'
    content += header('h2', 'Methods')

    return content

def gen_method(method: dict, file_content: str) -> str:
    content = header('h3', method['name'], ['code'])
    docstring = method['docstring']
    if docstring is None:
        return content + SEPARATOR
    
    description = text(docstring.short_description or '', newline=True)
    # In some cases, the whole docstring text will be parsed in the long_description.
    # Avoid appending it in that case.
    if isinstance(docstring.long_description, str) and docstring.long_description.find('Parameters') != -1:
        print(docstring.params)
        print('========>', docstring.long_description)
        warnings.warn(f'[{method["name"]}] failed to parse docstrings. Make sure the format is correct. Check guidelines if needed.', UserWarning)
    else: 
        description += text(docstring.long_description or '', newline=True)
        
    description = dedup_newlines(description)

    # TODO: refactor, synology_api.core_package.Package.easy_install don't have internal API, but it has a docstring.
    internal_api = parse_method_api(method['name'], file_content)

    parameters = ''
    if docstring.params:
        parameters = header('h4', 'Parameters')
        parameters_body = ''
        for param in docstring.params:
            validate_str(method['name'] + ' - params', [param.arg_name, param.type_name, param.description])
            parameters_body += text(param.arg_name or '', ['bold', 'italic'])
            parameters_body += text(param.type_name or '', ['code'], newline=True)
            parameters_body += text(dedup_newlines(param.description or ''), newline=True)
            parameters_body += NEWLINE
        parameters += div(content=parameters_body, spacing='padding', side='left', size='md')
    
    returns = ''
    if docstring.returns:
        validate_str(method['name'] + ' - returns', [docstring.returns.type_name, docstring.returns.description])
        returns = header('h4', 'Returns')
        returns_body = text(docstring.returns.type_name or '', ['code'], newline=True)
        returns_body += text(dedup_newlines(docstring.returns.description or ''), newline=True)
        returns += div(content=returns_body, spacing='padding', side='left', size='md')

    example_return = ''
    example_match = re.search(EXAMPLE_RETURN_PATTERN, method.get('docstring_text', ''))
    if example_match:
        example_return = header('h4', 'Example return')
        example_return += details(summary='Click to expand', content=example_match.group(2))

    content += description
    content += internal_api
    content += parameters
    content += returns
    content += example_return
    content += SEPARATOR
    content = insert_admonitions(content)

    return content

def write(path: str, content: str):
    with open(path, 'w', encoding="utf-8") as f:
        print('Writing into:', path)  
        f.write(content)

def main():
    parser = init_parser()
    files, parse_api_list, parse_docs = validate_args(parser)

    ### Generation for Getting Started/Supported APIs with all the APIs user per class.
    supported_apis = gen_supported_apis()

    for file_name in files:
        doc_content = ''
        file_path = join(PARSE_DIR, file_name)
        print('Processing: ' + file_name)
        with open(file_path, 'r', encoding="utf-8") as f: 
            file_content = f.read()
            docstrings = get_docstrings(file_content)
            if docstrings is None:
                warnings.warn(f'Failed to parse {file_name}', UserWarning)
                continue

            classes = [c for c in docstrings["content"] if not is_private(c['name'])]
            classes_names = [c['name'] for c in classes]
            for i, class_item in enumerate(classes):
                supported_apis += parse_class_apis(class_item['name'], file_content, file_name)
                doc_content += gen_header(
                    class_item['name'], 
                    class_item['docstring_text'],
                    classes=classes_names
                )

                methods = [m for m in class_item['content'] if not is_private(m['name'])]
                for method in methods:
                    doc_content += gen_method(method, file_content)

        # Write to md files if the args were set
        if parse_docs: 
            write(DOCS_DIR + file_name.replace('.py', '.md'), doc_content)
        print('='*20)
    # Write to md files if the args were set
    if parse_api_list:
        write(API_LIST_FILE, supported_apis)
        
if __name__ == "__main__":
    main()