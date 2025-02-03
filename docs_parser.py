import re
import yaml
from os import listdir
from os.path import isfile, join
from docstring_extractor import get_docstrings

DOCS_TRACKER = './docs_status.yaml'
PARSE_DIR = './synology_api'
DOCS_DIR = './documentation/docs/apis/'
EXCLUDED_FILES = {'__init__.py', 'auth.py', 'error_codes.py', 'exceptions.py', 'utils.py'}

ADMONITIONS = [
    {'pattern': r'(Note:)(.*)', 'replacement': ':::note \n'},
    {'pattern': r'(Info:)(.*)', 'replacement': ':::info \n'},
    {'pattern': r'(Tip:)(.*)', 'replacement': ':::tip \n'},
    {'pattern': r'(Warning:)(.*)', 'replacement': ':::warning \n'},
    {'pattern': r'(Danger:)(.*)', 'replacement': ':::danger \n'},
]

def get_apis():
    with open (DOCS_TRACKER, 'r') as stream:
        return yaml.safe_load(stream)

def is_private(signature: str) -> bool:
    return signature.startswith('_')

def get_docs_status_admonition(status: str) -> str:
    if status == 'partial':
        return ':::warning \n This API is partially documented or under construction. \n:::\n'
    elif status == 'not_started':
        return ':::warning \n This API is not documented yet.\n:::\n'
    else:
        return ''

def gen_class_doc(class_name: str, class_doc: str) -> str:
    display_order = 0
    docs_status = 'not_started'

    for i, api in enumerate(get_apis()):
        key = (list(api.keys())[0])
        if key == class_name:
            display_order = i
            docs_status = api[key]['status']

    content = ''

    # Set position 1 for BaseApi, and alphabetically for the rest
    if class_name == "BaseApi":
        content += f'---\nsidebar_position: 1\ntitle: {class_name}\n---\n\n'
    else: 
        content += f'---\nsidebar_position: {display_order + 2}\ntitle: {class_name}\n---\n\n'
    
    content += f'# {class_name} API\n'
    content += get_docs_status_admonition(docs_status)
    content += '## Overview\n'

    # Add markdown styling
    class_doc = class_doc.replace('Supported methods', '### Supported methods')
    class_doc = class_doc.replace('Getters', '**Getters**')
    class_doc = class_doc.replace('Setters', '**Setters**')
    class_doc = class_doc.replace('Actions', '**Actions**')

    content += class_doc + '\n'
    content += '## Methods\n'

    return content

def gen_method_doc(method_name: str, method_doc: str) -> str:
    content = f'### `{method_name}`\n'

    details_open = '#### Example return\n<details>\n<summary>Click to open example</summary>'

    # Remove section separators
    method_doc = re.sub(r'---.*', '', method_doc)

    # Add markdown headers
    method_doc = method_doc.replace('Parameters', '#### Parameters')
    method_doc = method_doc.replace('Returns', '#### Returns')

    # Add admonitions
    for pattern, replacement in ADMONITIONS:
        matches = re.findall(pattern, method_doc)
        for match in matches:
            method_doc = method_doc.replace(match[0], replacement)
            method_doc = method_doc.replace(match[1], f'{match[1]}\n:::\n')

    # Add markdown styling for param and return types
    params_pattern = r'(.*[a-z])\s:\s([a-z].*)'
    return_pattern = r'(#### Returns\n\n)(.*)'

    method_doc = re.sub(params_pattern, r'_**\1**_ `\2`  ', method_doc)
    method_doc = re.sub(return_pattern, r'\1`\2`  ', method_doc)  

    # Add details for example return to avoid clutter
    method_doc = method_doc.replace('Example return', details_open)
    if method_doc.find('<details>') != -1: # Avoid orphaned closing tag
        method_doc += '\n</details>\n\n'

    # Add separator
    content += method_doc + '\n\n\n---\n\n\n'

    return content

def main():
    files = listdir(PARSE_DIR)

    for file in files:
        if not isfile(join(PARSE_DIR, file)) or file in EXCLUDED_FILES:
            files.remove(file)

    for file_path in files:
        doc_content = ''

        with open(join(PARSE_DIR, file_path), 'r', encoding="utf-8") as f:
            try: 
                docstrings = get_docstrings(f)
            except Exception as e:
                print('cannot parse docstrings for', file_path, e)
                continue

            for class_type in docstrings["content"]:
                if is_private(class_type['name']):
                    continue
                doc_content += gen_class_doc(class_type['name'], class_type['docstring_text'])
                
                for method in class_type['content']:
                    if is_private(method['name']):
                        continue
                    doc_content += gen_method_doc(method['name'], method['docstring_text'])
        
        # Write to md file
        docs_file_path = DOCS_DIR + file_path.replace('py', 'md')
        with open(docs_file_path, 'w') as f:
            print('writing into', docs_file_path)
            f.write(doc_content)

if __name__ == "__main__":
    main()