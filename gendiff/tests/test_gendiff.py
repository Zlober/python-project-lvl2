import os
from gendiff import generate_diff
import pytest


path = os.path.join('gendiff', 'tests', 'fixtures')


@pytest.fixture
def result():
    with open(os.path.join(path, 'result')) as file:
        file = file.read()
    return file


def test_json(result):
    file1 = os.path.join(path, 'file1.json')
    file2 = os.path.join(path, 'file2.json')
    assert generate_diff(file1, file2) == result


def test_yaml(result):
    file1 = os.path.join(path, 'file1.yaml')
    file2 = os.path.join(path, 'file2.yaml')
    assert generate_diff(file1, file2) == result