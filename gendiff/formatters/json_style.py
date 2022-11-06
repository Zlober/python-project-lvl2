import json


def json_style(value):
    """Format in JSON style."""
    return json.dumps(value, indent=4)
