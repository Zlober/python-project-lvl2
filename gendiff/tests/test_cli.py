"""Cli test."""
import os
from gendiff.core import generate_diff


def files(file_name):
    """Make path to file.

    Args:
        file_name: name of file

    Returns:
        path to file
    """
    return os.path.join('gendiff', 'tests', 'fixtures', file_name)


def test_usupported_formatter():
    expected = 'Unsupported formatter'
    actual = generate_diff(
        files('simple_file1.json'), files('simple_file1.json'), 'blabla',
    )
    assert actual == expected
