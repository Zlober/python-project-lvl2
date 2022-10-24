import argparse
import json


def cmd():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument_group()
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    keys = file1.keys() | file2.keys()
    keys = sorted(keys)
    result = '{\n'
    spaces = ' ' * 2
    for key in keys:
        if key in file1 and key not in file2:
            result += f'{spaces}- {key}: {file1[key]}\n'
        elif key in file2 and key not in file1:
            result += f'{spaces}+ {key}: {file2[key]}\n'
        elif file1[key] != file2[key]:
            result += f'{spaces}- {key}: {file1[key]}\n'
            result += f'{spaces}+ {key}: {file2[key]}\n'
        else:
            result += f'{spaces}  {key}: {file1[key]}\n'
    result += '}'
    return result.lower()
