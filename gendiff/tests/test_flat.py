from gendiff import generate_diff
import os
import pytest

@pytest.fixture
def expected():
    result = os.path.join('gendiff', 'tests', 'fixtures', 'expected', 'flat')
    with open(result) as file:
        result = file.read()
    return result


def test_json(expected):
    file1 = os.path.join('gendiff', 'tests', 'fixtures', 'flat', 'file1.json')
    file2 = os.path.join('gendiff', 'tests', 'fixtures', 'flat', 'file2.json')
    assert generate_diff(file1, file2) == expected


def test_yaml(expected):
    file1 = os.path.join('gendiff', 'tests', 'fixtures', 'flat', 'file1.yaml')
    file2 = os.path.join('gendiff', 'tests', 'fixtures', 'flat', 'file2.yaml')
    assert generate_diff(file1, file2) == expected


def test_yaml_extension(expected):
    file1 = os.path.join('gendiff', 'tests', 'fixtures', 'flat', 'file1.yml')
    file2 = os.path.join('gendiff', 'tests', 'fixtures', 'flat', 'file2.yml')
    assert generate_diff(file1, file2) == expected
