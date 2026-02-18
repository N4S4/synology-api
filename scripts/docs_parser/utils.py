import warnings
from pathlib import Path

#############
#   Utils   #
#############

def _is_private(name: str) -> bool:
    return name.startswith("_")

def write(path: Path, content: str):
    with open(path, 'w', encoding="utf-8") as f:
        print('Writing into:', path)
        f.write(content)

class WarningCatcher:
    warnings = []

    def __call__(self, message, category, filename, lineno, file=None, line=None):
        msg = warnings.formatwarning(message, category, filename, lineno, line)
        WarningCatcher.warnings.append(msg)

    @staticmethod
    def has_warnings():
        return bool(WarningCatcher.warnings)

    @staticmethod
    def print_warnings():
        for w in WarningCatcher.warnings:
            print(w, end='')
