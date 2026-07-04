import os


def create_directory(directory):
    """
    Create directory if it doesn't exist.
    """

    if not os.path.exists(directory):
        os.makedirs(directory)
