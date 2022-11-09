"""Gendiff module."""
import argparse

from gendiff.core import generate_diff


def main():
    """Print output of gendiff module."""
    arguments = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    arguments.add_argument('first_file')
    arguments.add_argument('second_file')
    arguments.add_argument_group()
    arguments.add_argument(
        '-f', '--format', help='set format of output', default='stylish',
    )
    args = arguments.parse_args()
    print(generate_diff(
        args.first_file,
        args.second_file,
        args.format,
    ))


if __name__ == '__main__':
    main()
