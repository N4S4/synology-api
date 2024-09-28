import json,sys
# my_package/my_module.py
__all__ = ['merge_dicts', 'make_folder_meta_list_from_path', 'parse_config']

def merge_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

def make_folder_meta_list_from_path( path):
    """
    Create a list of folder metadata dictionaries from a given path.

    Args:
        path (str): The file path to be split into folder metadata.

    Returns:
        list: A list of dictionaries containing folder metadata.
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
