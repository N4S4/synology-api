from pathlib import Path

####################
# Config Constants #
####################

_BASE_DIR = Path(__file__).resolve().parents[2]

DOCS_TRACKER = _BASE_DIR / "docs_status.yaml"
PARSE_DIR = _BASE_DIR / "synology_api"
API_LIST_FILE = _BASE_DIR / "documentation" / "docs" / "apis" / "readme.md"
DOCS_DIR = _BASE_DIR / "documentation" / "docs" / "apis" / "classes"

EXCLUDED_FILES = {'__init__.py', 'auth.py', 'base_api.py',
                  'error_codes.py', 'exceptions.py', 'utils.py'}