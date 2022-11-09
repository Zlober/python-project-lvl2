"""Gendiff module."""
from gendiff.core import cli, generate_diff
import argparse


def main():
    """Print output of gendiff module."""
    arguments = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    arguments.add_argument('first_file')
    arguments.add_argument('second_file')
    arguments.add_argument_group()
    arguments.add_argument('-f', '--format', help='set format of output', default='stylish')
    args = arguments.parse_args()
    file1, file2, output_format = cli()
    print(generate_diff(
        args.first_file,
        args.second_file,
        args.format,
    ))


if __name__ == '__main__':
    main()
