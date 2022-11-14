"""Module for create a tree of difference."""
from gendiff.parser import parser

from gendiff.formatter import formatting
from gendiff.tree import diff


def generate_diff(file1, file2, output_format='stylish'):
    """Generate stylized output of diff between two files.

    Args:
        file1: path to file1
        file2: path to file2
        output_format: format of the output

    Returns:
        str of difference file in select format
    """
    file1 = parser(file1)
    file2 = parser(file2)
    diff_dict = diff(file1, file2)
    return formatting(diff_dict, output_format)
