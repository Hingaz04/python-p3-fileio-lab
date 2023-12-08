

def write_file(file_name, file_content):
    """
    Write content to a file.

    Args:
        file_name (str): The name of the file (including path if needed).
        file_content (str): The content to be written to the file.

    Returns:
        None
    """
    with open(file_name + ".txt", "w") as file:
        file.write(file_content)


def append_to_file(file_name, append_content):
    """
    Append content to an existing file.

    Args:
        file_name (str): The name of the file (including path if needed).
        append_content (str): The content to be appended to the file.

    Returns:
        None
    """
    with open(file_name + ".txt", "a") as file:
        file.write(append_content)


def read_file(file_name):
    """
    Read content from a file.

    Args:
        file_name (str): The name of the file (including path if needed).

    Returns:
        str: The content of the file.
    """
    with open(file_name + ".txt", "r") as file:
        content = file.read()
    return content
