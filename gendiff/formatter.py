"""Formatting module."""
from gendiff.formatters import json_style, plain, stylish


def formatting(tree, format_type):
    """Formmating output.

    Args:
        tree: dict
        format_type: type of format

    Returns:
        formatted str
    """
    format_types = {
        'stylish': stylish,
        'plain': plain,
        'json': json_style,
    }
    formatter = format_types.get(format_type)
    if formatter is not None:
        return formatter(tree)
    raise Exception('Unsupported formatter')
