import argparse
from gendiff.parser import parser
from gendiff.formatters import stylish, plain, json_style


def cli():
    """Parse arguments."""
    param = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    param.add_argument('first_file')
    param.add_argument('second_file')
    param.add_argument_group()
    param.add_argument('-f', '--format',
                       choices=['stylish', 'plain', 'json'],
                       default='stylish',
                       help='set format of output')
    args = param.parse_args()
    return args.first_file, args.second_file, args.format


def generate_diff(file1, file2, output_format='stylish'):
    """Generate stylized output of diff between two files."""
    format_type = {
        'stylish': stylish,
        'plain': plain,
        'json': json_style
    }
    file1 = parser(file1)
    file2 = parser(file2)
    diff_dict = diff(file1, file2)
    return format_type[output_format](diff_dict)


def diff(dict1, dict2):
    """Generate tree"""
    result = {}
    keys = dict1.keys() | dict2.keys()
    deleted = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    for key in sorted(keys):
        if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
            result[key] = {
                'type': 'children',
                'value': diff(dict1[key], dict2[key])
            }
        elif key in added:
            result[key] = {
                'type': 'added',
                'value': dict2[key]
            }
        elif key in deleted:
            result[key] = {
                'type': 'deleted',
                'value': dict1[key]
            }
        elif dict1[key] == dict2[key]:
            result[key] = {
                'type': 'unchanged',
                'value': dict1[key]
            }
        elif key in dict1 and key in dict2:
            result[key] = {
                'type': 'updated',
                'old': dict1[key],
                'new': dict2[key]
            }
    return result
