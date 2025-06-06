def to_uppercase(text):
    """
    Convert a given string to uppercase.
    Parameters:
    text (str): The string to convert.
    Returns:
    str: The uppercase version of the string. Returns an empty string if the input is None.
    """
    if text is None:
        return ''
    return text.upper()

def to_lowercase(text):
    """
    Convert a given string to lowercase.
    Parameters:
    text (str): The string to convert.
    Returns:
    str: The lowercase version of the string. Returns an empty string if the input is None.
    """
    if text is None:
        return ''
    return text.lower()

def is_palindrome(text):
    """
    Check if a given string is a palindrome.
    A palindrome is a string that reads the same forward and backward, ignoring spaces and case.
    Parameters:
    text (str): The string to check.
    Returns:
    bool: True if the string is a palindrome, False otherwise. Returns False if the input is None.
    """
    if text is None:
        return False
    normalized = ''.join(text.lower().split())
    return normalized == normalized[::-1]

def remove_whitespace(text):
    """
    Remove all whitespace from a given string.
    Parameters:
    text (str): The string to process.
    Returns:
    str: The string with all whitespace removed. Returns an empty string if the input is None.
    """
    if text is None:
        return ''
    return ''.join(text.split())