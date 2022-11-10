"""JSON files diff test."""
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


def open_files(file_path):
    """Read the file.

    Args:
        file_path: path to file

    Returns:
        data
    """
    with open(file_path) as txt_file:
        txt_file = txt_file.read()
    return txt_file


def test1_simple_string():
    """Test 1."""
    actual = generate_diff(
        files('simple_file1.json'), files('simple_file2.json'),
    )
    assert actual == open_files(files('simple.txt'))


def test2_simple_plain():
    """Test 2."""
    actual = generate_diff(
        files('simple_file1.json'), files('simple_file2.json'), 'plain',
    )
    assert actual == open_files(files('simple_plain.txt'))


def test3_simple_json():
    """Test 3."""
    actual = generate_diff(
        files('simple_file1.json'), files('simple_file2.json'), 'json',
    )
    assert actual == open_files(files('simple_json.txt'))


def test4_complex_string():
    """Test 4."""
    actual = generate_diff(
        files('complex_file1.json'), files('complex_file2.json'),
    )
    assert actual == open_files(files('complex.txt'))


def test5_complex_plain():
    """Test 5."""
    actual = generate_diff(
        files('complex_file1.json'), files('complex_file2.json'), 'plain',
    )
    assert actual == open_files(files('complex_plain.txt'))


def test6_complex_json():
    """Test 6."""
    actual = generate_diff(
        files('complex_file1.json'), files('complex_file2.json'), 'json',
    )
    assert actual == open_files(files('complex_json.txt'))
