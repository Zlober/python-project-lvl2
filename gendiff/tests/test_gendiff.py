import os
from gendiff import generate_diff


def test_main():
    result = open(os.path.join('gendiff', 'tests', 'fixtures', 'result')).read()
    file1 = os.path.join('gendiff', 'tests', 'fixtures', 'file1.json')
    file2 = os.path.join('gendiff', 'tests', 'fixtures', 'file2.json')
    assert generate_diff(file1, file2) == result
