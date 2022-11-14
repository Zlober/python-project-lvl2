"""Cli test."""
import os

import pytest

from gendiff.core import generate_diff


def files(file_name):
    """Make path to file.

    Args:
        file_name: name of file

    Returns:
        path to file
    """
    return os.path.join('gendiff', 'tests', 'fixtures', file_name)


def test_unsupported_formatter():
    with pytest.raises(Exception) as expected:
        generate_diff(
            files('simple_file1.json'), files('simple_file1.json'), 'blabla',
        )
        assert expected.value == 'Unsupported formatter'
