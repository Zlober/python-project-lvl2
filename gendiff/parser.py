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
            return json.load(files)
        if 'yaml' or 'yml' in files.name:
            return yaml.safe_load(files)
        raise Exception('Unrecognized format: {0}'.format(
            files.name,
        ))
