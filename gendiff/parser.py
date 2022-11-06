import json
import yaml


def parser(file):
    """Parse a file to Python dict."""
    with open(file) as file:
        if 'json' in file.name:
            file = json.load(file)
        else:
            file = yaml.safe_load(file)
    return file
