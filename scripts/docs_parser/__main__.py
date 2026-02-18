import argparse
import sys
import warnings

from .config import API_LIST_FILE, EXCLUDED_FILES, DOCS_DIR, DOCS_TRACKER, PARSE_DIR
from .parser import get_docs_status, extract_file_info
from .markdown_generator import gen_doc_header, gen_doc_method, gen_supported_apis, header
from .utils import WarningCatcher, write

# Setup warning catcher
warning_catcher = WarningCatcher()
warnings.showwarning = warning_catcher

###############
#   Parsing   #
###############

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

################
# Main routine #
################

files, parse_api_list, parse_docs, exit_on_warning = parse_and_validate_args()

# Parse API documentation status
docs_status_info = get_docs_status(DOCS_TRACKER)

files_info = {}
supported_apis = {}

for file_name in files:
    print('Processing: ' + file_name)
    file_info = extract_file_info(PARSE_DIR / file_name, verbose=False)

    supported_apis.update({
        class_name: (file_name, class_info['api_names']) for class_name, class_info in file_info['classes'].items()
    })

    if parse_docs:
        doc_content = ''

        # Sort classes by class index (= position in the file) [python < 3.7's dict() safety]
        sorted_class_items = sorted(file_info['classes'].items(), key=lambda keyval: keyval[1]['index'])
        for class_name, class_info in sorted_class_items:
            doc_content += gen_doc_header(
                class_name,
                class_info['docstring'],
                class_info['index'],
                tuple(c_name for c_name, _ in sorted_class_items[1:]),
                docs_status_info=docs_status_info
            )

            if class_info['methods']:
                doc_content += header('h2', 'Methods')

                for method_name, method_info in class_info['methods'].items():
                    doc_content += gen_doc_method(
                        method_name,
                        method_info['docstring'],
                        method_info['internal_api']
                    )

        # Write file's documentation
        write(DOCS_DIR / file_name.replace('.py', '.md'), doc_content)
        print('='*20)

    files_info[file_name] = file_info

# Write API list summary
if parse_api_list:
    print('Processing Supported APIs')
    content = gen_supported_apis(supported_apis)
    write(API_LIST_FILE, content)

# If warnings, display them and exit(1)
if exit_on_warning and warning_catcher.has_warnings():
    print('\n\n', r"/!\ Docs generation has failed because of the following warnings /!\ ", '\n')
    warning_catcher.print_warnings()
    sys.exit(1)

# All good
sys.exit(0)