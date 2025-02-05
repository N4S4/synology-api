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
DOCS_DIR = './documentation/docs/apis/'
EXCLUDED_FILES = {'__init__.py', 'auth.py', 'error_codes.py', 'exceptions.py', 'utils.py'}

####################
# String Constants #
####################
META_TAG = '---\n'
SEPARATOR = '\n\n\n---\n\n\n'
NEWLINE = '  \n'
ADMONITIONS = [
    {'pattern': r'(Note:)(.*)', 'level': 'note'},
    {'pattern': r'(Info:)(.*)', 'level': 'info'},
    {'pattern': r'(Tip:)(.*)', 'level': 'tip'},
    {'pattern': r'(Warning:)(.*)', 'level': 'warning'},
    {'pattern': r'(Danger:)(.*)', 'level': 'danger'},
]
EXAMPLE_RETURN_PATTERN = r'(?s)(Example return\n-.*)(```.*```)'

####################
# Style Generators #
###################
def __stylize(text: str, styles: list[str]) -> str:
    content = ''
    for style_str in styles:
        if style_str == 'code':
            content += '`'
        elif style_str == 'bold':
            content += '**'
        elif style_str == 'italic':
            content += '_'
        elif style_str == 'underline':
            content += '___'
        else:
            warnings.warn(f'Unknown style: {style_str}', UserWarning)
        
    content += text

    for style_str in reversed(styles):
        if style_str == 'code':
            content += '`'
        elif style_str == 'bold':
            content += '**'
        elif style_str == 'italic':
            content += '_'
        elif style_str == 'underline':
            content += '___'
        
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

def div(content: str, spacing: str = '', side: str = '', size: str = '') -> str:
    """Generate div element"""
    return f'<div class="{spacing}-{side}--{size}">\n{content}\n</div>\n'

def details(summary: str, content: str) -> str:
    """Generate details element"""
    details = f'<details>\n<summary>{summary}</summary>'
    details += f'\n{content}\n</details>\n'
    return details

def metadata(class_name: str) -> tuple[str, str]:
    """Generate front matter header"""
    for i, api in enumerate(get_apis()):
        key = (list(api.keys())[0])
        if key == class_name:
            display_order = 1 if class_name == 'BaseApi' else i + 2
            docs_status = api[key]['status']
    status_indicator = '✅' if docs_status == 'finished' else '🚧'

    content = META_TAG
    content += f'sidebar_position: {display_order}\n'
    content += f'title: {status_indicator} {class_name}\n'
    content += META_TAG
    
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
    parser.add_argument('-e', '--excluded',
                        action='store_true',
                        help='Show a list of the excluded files to parse.')
    
    return parser

def get_files_to_parse() -> list[str]:
    files = listdir(PARSE_DIR)
    return [file for file in files if isfile(join(PARSE_DIR, file)) and file not in EXCLUDED_FILES]

def validate_args(parser: argparse.ArgumentParser) -> list[str]:
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
    if args.excluded:
        print('Excluded files:')
        for file in EXCLUDED_FILES:
            print(file)
        sys.exit(1)

    if args.all:
        files = get_files_to_parse()
    elif args.file:
        files = args.file

    return files

def validate_str(context: str, strs: list[str]):
    for current in strs:
        if not isinstance(current, str):
            warnings.warn(f'[{context}] Invalid string: {current}', UserWarning)

def get_apis():
    with open (DOCS_TRACKER, 'r') as stream:
        return yaml.safe_load(stream)

def is_private(signature: str) -> bool:
    return signature.startswith('_')

def insert_admonitions(content: str) -> str:
    for adm in ADMONITIONS:
        content = re.sub(adm['pattern'], lambda match: admonition(adm['level'], match.group(2)), content)
    return content

def gen_header(class_name: str, docstring: str) -> str:
    content, docs_status = metadata(class_name)
    content += header('h1', class_name)
    content += status_disclaimer(docs_status)
    content += header('h2', 'Overview')

    docstring = docstring.replace('Supported methods:', header('h3', 'Supported methods'))
    docstring = docstring.replace('Getters', text('Getters', ['bold']))
    docstring = docstring.replace('Setters', text('Setters', ['bold']))
    docstring = docstring.replace('Actions', text('Actions', ['bold']))

    content += docstring + '\n'
    content += header('h2', 'Methods')

    return content

def gen_method(method: dict) -> str:
    content = header('h3', method['name'], ['code'])
    docstring = method['docstring']
    if docstring is None:
        return content + SEPARATOR
    
    description = text(docstring.short_description or '', newline=True)
    description += text(docstring.long_description or '', newline=True)
    description = dedup_newlines(description)

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
    content += parameters
    content += returns
    content += example_return
    content += SEPARATOR
    content = insert_admonitions(content)

    return content

def write(file_name: str, content: str):
    docs_file_path = DOCS_DIR + file_name.replace('.py', '.md')
    with open(docs_file_path, 'w', encoding="utf-8") as f:
        print('Writing into:', docs_file_path)  
        f.write(content)

def main():
    parser = init_parser()
    files = validate_args(parser)

    for file_name in files:
        doc_content = ''
        file_path = join(PARSE_DIR, file_name)
        print('Parsing: ' + file_name)
        with open(file_path, 'r', encoding="utf-8") as f:
            docstrings = get_docstrings(f)
            if docstrings is None:
                continue

            for class_type in docstrings["content"]:
                if is_private(class_type['name']):
                    continue
                print('Building MD for: ' + class_type['name'])
                doc_content += gen_header(class_type['name'], class_type['docstring_text'])

                for method in class_type['content']:
                    if is_private(method['name']):
                        continue
                    doc_content += gen_method(method)
          
        write(file_name, doc_content)
        print('\n', '='*20, '\n')
        
if __name__ == "__main__":
    main()