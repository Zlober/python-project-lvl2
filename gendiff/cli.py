"""Cli module."""
import argparse


def argument_parser():
    """Parser argument."""
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
    return args
