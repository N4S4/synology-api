"""Utility functions for Synology API operations."""
import json
import secrets
import sys
# my_package/my_module.py
__all__ = ['merge_dicts', 'make_folder_meta_list_from_path', 'parse_config']

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
