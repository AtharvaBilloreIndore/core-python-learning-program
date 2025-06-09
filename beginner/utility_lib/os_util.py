import os
def get_current_working_directory():
    """
    Get the current working directory.
    Returns:
    str: The path of the current working directory.
    """
    return os.getcwd()

def file_exists(path):
    """
    Check if a file exists at the specified path.
    Parameters:
    path (str): The path to the file.
    Returns:
    bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(path)

def dir_exists(path):
    """
    Check if a directory exists at the specified path.
    Parameters:
    path (str): The path to the directory.
    Returns:
    bool: True if the directory exists, False otherwise.
    """
    return os.path.isdir(path)

def create_directory(path):
    """
    Create a directory at the specified path if it does not already exist.
    Parameters:
    path (str): The path where the directory should be created.
    Returns:
    bool: True if the directory was created, False if it already exists.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False