import ast
import yaml

from pathlib import Path
from typing import Any, Optional
from docstring_parser import Docstring, numpydoc

from .utils import _is_private

# Ensure numpydoc parser
parse_docstring = numpydoc.parse

# def _parse_docstring(text: Optional[str]) -> Optional[Docstring]:
#     if not text:
#         return None
#     return parse_docstring(text)

#############################
# api_name extraction utils #
#############################

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

###############################
# ast-tree extraction helpers #
###############################

def _extract_docstring(node: ast.Module | ast.FunctionDef | ast.ClassDef) -> Optional[Docstring]:
    docstring_str = ast.get_docstring(node, clean=True)
    return parse_docstring(docstring_str) if docstring_str else None

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

####################
#   Main methods   #
####################

# -> ast file parser

def extract_file_info(file_path: Path, verbose: bool = False) -> dict[str, dict[str, Any]]:
    """
    AST-parse a Python file and extract class/method docstrings + inferred API names.

    Docstrings are returned as `docstring_parser.Docstring` objects (or None if absent/unparseable).

    Parameters
    ----------
    docs_status_tracker : Path
        Path to project's docs_status.yaml file.

    Returns
    -------
    dict[str, dict[str, int|str]]
        Dictionary of the form
        ```
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
        ```
    """
    # -- Debug (verbose) print helper --

    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    # ----------------------------------

    vprint(f"Parsing file `{file_path.name}` ...")

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    # Generate ast tree
    try:
        tree = ast.parse(source, filename=file_path)
    except SyntaxError as e:
        raise SyntaxError(f"Failed to parse {file_path}") from e

    # File's main data structure
    file_info: dict[str, Any] = {
        'classes': {},
        'docstring': _extract_docstring(tree) # File-level dosctring
    }

    # Iterate over classes
    cls_position_index = 0
    for cls_node in tree.body:
        if not isinstance(cls_node, ast.ClassDef) or _is_private(cls_node.name):
            continue

        vprint(f"    Parsing class `{cls_node.name}` ...")

        cls_name = cls_node.name
        cls_doc = _extract_docstring(cls_node) # Class-level docstring
        cls_api = _extract_class_api_name(cls_node) # Class-level attribute `_API_NAME = ...` or `_api_name = ...`

        vprint(f"        _API_NAME: `{cls_api}`")


        # Iterate over methods
        methods: dict[str, dict[str, Any]] = {}

        for mth_node in cls_node.body:
            if not isinstance(mth_node, ast.FunctionDef) or _is_private(mth_node.name):
                continue

            mth_name = mth_node.name
            vprint(f"        Parsing method `{mth_name}` ...")

            # Method-level info
            methods[mth_node.name] = {
                "docstring": _extract_docstring(mth_node),
                "internal_api": _extract_method_api_name(mth_node, parent_api_name=cls_api),
            }

            vprint(f"            internal_api: `{methods[mth_node.name]['internal_api']}`")

        # Class-level info
        file_info['classes'][cls_name] = {
            "index": cls_position_index,
            "docstring": cls_doc,
            "api_names": { # Gather all class's methods API names
                mth_info["internal_api"] for mth_info in methods.values() if mth_info["internal_api"]
            },
            "methods": methods,
        }

        cls_position_index += 1

    return file_info

# -> Doc status getter
def get_docs_status(docs_status_tracker: Path) -> dict[str, dict[str, int|str]]:
    """
    Extract documentation status and infer sidebar display order of implemented classes.

    Parameters
    ----------
    docs_status_tracker : Path
        Path to project's docs_status.yaml file.

    Returns
    -------
    dict[str, dict[str, int|str]]
        Dictionary of the form
        ```
        {
            'API_class_name' : {'display_order': <int>, 'status': <"partial", "finished", ...>},
            ...
        }
        ```
    """
    with open(docs_status_tracker, 'r') as stream:
        api_status_dict = yaml.safe_load(stream)

    # Generate sorted list of API names
    #  -> 'BaseApi' comes first, then alphabetical ordering
    api_names = ['BaseApi'] + sorted(api_status_dict.keys() - {'BaseApi'})

    return {
        api_name: {
            'display_order': pos,
            'status': api_status_dict[api_name]['status']
        } for pos, api_name in enumerate(api_names, start=1)
    }
