"""JSON files diff test."""
import os

from gendiff.core import generate_diff
from gendiff.tests import expected


def files(file_name):
    return os.path.join('gendiff', 'tests', 'fixtures', file_name)


def test1_simple_string():
    actual = generate_diff(files('simple_file1.json'),
                           files('simple_file2.json'),
                           )
    assert actual == expected.SIMPLE_STRING


def test2_simple_plain():
    actual = generate_diff(files('simple_file1.json'),
                           files('simple_file2.json'),
                           'plain')
    assert actual == expected.SIMPLE_PLAIN


def test3_simple_json():
    actual = generate_diff(files('simple_file1.json'),
                           files('simple_file2.json'),
                           'json')
    assert actual == expected.SIMPLE_JSON


def test4_complex_string():
    actual = generate_diff(files('complex_file1.json'),
                           files('complex_file2.json'),
                           )
    assert actual == expected.COMPLEX_STRING


def test5_complex_plain():
    actual = generate_diff(files('complex_file1.json'),
                           files('complex_file2.json'),
                           'plain')
    assert actual == expected.COMPLEX_PLAIN


def test6_complex_json():
    actual = generate_diff(files('complex_file1.json'),
                           files('complex_file2.json'),
                           'json')
    assert actual == expected.COMPLEX_JSON
