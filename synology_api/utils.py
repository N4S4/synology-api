"""Utility functions for Synology API operations."""
import json
import re
import secrets
import sys
# my_package/my_module.py
__all__ = ['merge_dicts', 'make_folder_meta_list_from_path',
           'get_data_for_request_from_file', 'generate_gecko_boundary', 'validate_path']

from pathlib import Path

from requests_toolbelt import MultipartEncoder


def merge_dicts(x, y):
    """
    Merge two dictionaries.

    Parameters
    ----------
    x : dict
        The first dictionary.
    y : dict
        The second dictionary.

    Returns
    -------
    dict
        A new dictionary containing the merged keys and values from both input dictionaries.
    """
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z


def make_folder_meta_list_from_path(path):
    """
    Create a list of folder metadata dictionaries from a given path.

    Parameters
    ----------
    path : str
        The file path to be split into folder metadata.

    Returns
    -------
    list of dict
        A list of dictionaries containing folder metadata for each folder in the path.
    """
    folder_list = []
    path_list = path.split('/')  # Split the path into components

    for folder in path_list:
        # Create a dictionary for each folder and append to the list
        folder_list.append({
            'alternatelink': '',
            'file_id': '',
            'mtime': 0,
            'parent_id': '',
            'title': '',
            'path': '/' + folder,
            'title': ''
        })

    return folder_list


def get_data_for_request_from_file(file_path: str, fields: list[tuple]):
    """
    Receive a file path and return a MultiPartEncoder for uploading it inside a request_data.

    Parameters
    ----------
    file_path : str
        The file path to be parsed.
    fields : list of tuple[str, str]
        Fields to create the MultiPartEncoder.

    Returns
    -------
    MultiPartEncoder
        MultiPartEncoder Object to send to the post request.
    """

    p = Path(file_path).expanduser().resolve()
    if not p.is_file():
        raise FileNotFoundError(f"File not found: {p}")

    size_value = p.stat().st_size
    boundary = generate_gecko_boundary()
    fields.append(("size", str(size_value)))
    fields.append(
        ("torrent", (p.name, p.open("rb"), "application/x-bittorrent")))

    enc = MultipartEncoder(fields=fields, boundary=boundary)
    return enc


def generate_gecko_boundary():
    """
    Generate a boundary for MultiPartEncoder.

    Returns
    -------
    str:
     The random boundary ----geckoformboundary{random_hex} for the MultiPartEncoder.
    """
    random_hex = secrets.token_hex(16)  # 16 byte = 32 caratteri esadecimali
    return f"----geckoformboundary{random_hex}"


def validate_path(path: str | list[str]) -> bool:
    """
    Validate the format of a Synology FileStation path.

    The function checks whether a given path string (or list of paths) follows
    the basic formatting rules required by Synology FileStation APIs.

    Parameters
    ----------
    path : str or list of str
        The path or list of paths to validate. Each path can represent
        either a file or directory.

    Returns
    -------
    bool
        True if the path (or all paths in the list) are valid according to
        FileStation rules, False otherwise.

    Notes
    -----
    - Must start with a forward slash ('/').
    - Must not contain any of the forbidden characters: * ? " < > |
    - May contain internal spaces (e.g., '/My Folder/file name.txt').
    - Must not end with a space, tab, or slash.
    - If the path contains a file extension, no spaces or characters are allowed
      after the last period (e.g., '/Media/script.log extra' is invalid).
    - Optionally allows paths without extensions (e.g., '/Media/script').

    Examples
    --------
    >>> validate_path('/Downloads/script.log')
    True
    >>> validate_path('/Downloads/script log.txt')
    True
    >>> validate_path('/Downloads/script')
    True
    >>> validate_path('/Downloads/script.log extra')
    False
    >>> validate_path('/Downloads/script.log ')
    False
    >>> validate_path('/Downloads/folder/')
    False
    >>> validate_path('Downloads/script.log')
    False
    """

    def _is_valid(single_path: str) -> bool:
        """
        Validate a single Synology FileStation path.

        Parameters
        ----------
        single_path : str
            The path to validate.

        Returns
        -------
        bool
            True if the given path is a valid Synology FileStation path.
        """
        path_pattern = re.compile(r'^/[^*?"<>|]+$')
        if not isinstance(single_path, str):
            return False

        if not path_pattern.match(single_path):
            return False

        if path[-1] in (' ', '\t', '/'):
            return False

        parts = single_path.rsplit('.', 1)
        if len(parts) == 2 and ' ' in parts[1]:
            return False

        return True

    if isinstance(path, str):
        return _is_valid(path)

    if isinstance(path, list):
        return all(isinstance(p, str) and _is_valid(p) for p in path)

    return False
