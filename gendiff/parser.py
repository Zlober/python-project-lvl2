"""Module to parse file."""
import json

import yaml


def parser(file_name):
    """Parse a file to Python dict.

    Args:
        file_name: path to file

    Returns:
        dict
    """
    with open(file_name) as files:
        if 'json' in files.name:
            files = json.load(files)
        else:
            files = yaml.safe_load(files)
        return files
