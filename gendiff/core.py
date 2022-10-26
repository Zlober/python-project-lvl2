import argparse
import json
import yaml


def cmd():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument_group()
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def generate_diff(file1, file2):
    file1 = parser(file1)
    file2 = parser(file2)
    keys = file1.keys() | file2.keys()
    keys = sorted(keys)
    result = '{\n'
    spaces = ' '
    for key in keys:
        if key in file1 and key not in file2:
            result += f'{spaces *2}- {key}: {file1[key]}\n'
        elif key in file2 and key not in file1:
            result += f'{spaces * 2}+ {key}: {file2[key]}\n'
        elif file1[key] != file2[key]:
            result += f'{spaces * 2}- {key}: {file1[key]}\n'
            result += f'{spaces * 2}+ {key}: {file2[key]}\n'
        else:
            result += f'{spaces * 4}{key}: {file1[key]}\n'
    result += '}'
    return result.lower()


def parser(file):
    with open(file) as file:
        if 'json' in file.name:
            file = json.load(file)
        else:
            file = yaml.safe_load(file)
    return file
