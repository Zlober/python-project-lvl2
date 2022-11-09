"""Output in json style."""
import json


def json_style(tree):
    """Format in JSON style.

    Args:
        tree: dict

    Returns:
        string in style
    """
    return json.dumps(tree, indent=4)
