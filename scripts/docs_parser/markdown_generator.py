import re
import warnings

from docstring_parser import Docstring
from typing import Any, Optional, Sequence

from .config import DOCS_TRACKER

####################
# String Constants #
####################

META_TAG = '---\n'
SEPARATOR = '\n\n\n---\n\n\n'
NEWLINE = '  \n'
AUTO_GEN_TAG = '\n<!-- ' + '-'*44 + ' -->\n'
AUTO_GEN_MESSAGE = '<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->'
AUTO_GEN_DISCLAIMER = AUTO_GEN_TAG + AUTO_GEN_MESSAGE + AUTO_GEN_TAG + NEWLINE

DOCS_STATUS_INDICATOR = {
    'finished': '✅',
    'partial': '🚧',
    'not_started': '🚧'
}

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
            parameters_body += text(param.description or '', newline=True)
            parameters_body += NEWLINE
        parameters += div(content=parameters_body,
                          spacing='padding', side='left', size='md')
    return parameters + NEWLINE

def get_docstring_example_return(docstring: Docstring) -> str | None:
    example = docstring.examples
    if len(example) != 1 or not example[0].description:
        return None
    code_block_match = re.match(EXAMPLE_RETURN_PATTERN, example[0].description)
    if code_block_match:
        return code_block_match.group(0)
    return None

###################
# Docs generation #
###################

def gen_supported_apis(supported_apis: dict[str, dict]) -> str:
    content = META_TAG
    content += 'sidebar_position: 1\n'
    content += 'title: Supported APIs\n'
    content += META_TAG
    content += AUTO_GEN_DISCLAIMER
    content += header('h1', 'Supported APIs')
    content += text("At the moment there are quite a few APIs implemented. They could be "
                    "totally or partially implemented, for specific documentation about "
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

def gen_doc_metadata(class_name: str, docs_status_info: dict) -> tuple[str, str]:
    """Generate front matter header"""
    docs_status, display_order, status_indicator = '', '', ''

    if class_name in docs_status_info:
        docs_status, display_order = (docs_status_info[class_name][key] for key in ('status', 'display_order'))
        try:
            status_indicator = DOCS_STATUS_INDICATOR[docs_status]
        except KeyError:
            warnings.warn(
                f"Unknown documentation status '{docs_status}' for class '{class_name}'. "
                f"Possible values: '{'\', \''.join(DOCS_STATUS_INDICATOR.keys())}'. "
                f"Please update `{DOCS_TRACKER.name}` accordingly."
            , UserWarning)
    else:
        warnings.warn(
            f"Class '{class_name}' is missing from `{DOCS_TRACKER.name}`. "
            f"Please update `{DOCS_TRACKER.name}` accordingly."
        , UserWarning)

    content = META_TAG
    content += f'sidebar_position: {display_order}\n'
    content += f'title: {status_indicator} {class_name}\n'
    content += META_TAG
    content += AUTO_GEN_DISCLAIMER

    return (content, docs_status)

def gen_doc_header(class_name: str, docstring: Docstring, class_index: int, additional_classes: Sequence[str], docs_status_info: dict) -> str:
    content = ''
    docs_status = ''

    if class_index == 0:
        content, docs_status = gen_doc_metadata(class_name, docs_status_info)

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
