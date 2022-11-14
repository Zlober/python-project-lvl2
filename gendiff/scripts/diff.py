"""Gendiff module."""
from gendiff.core import generate_diff

from gendiff.cli import argument_parser


def main():
    """Print output of gendiff module."""
    first_file, second_file, output_format = argument_parser()
    print(generate_diff(
        first_file,
        second_file,
        output_format,
    ))


if __name__ == '__main__':
    main()
