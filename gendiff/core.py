"""Module for create a tree of difference."""
from gendiff.formatters import json_style, plain, stylish
from gendiff.parser import parser


def generate_diff(file1, file2, output_format='stylish'):
    """Generate stylized output of diff between two files.

    Args:
        file1: path to file1
        file2: path to file2
        output_format: format of the output

    Returns:
        str of difference file in select format
    """
    format_type = {
        'stylish': stylish,
        'plain': plain,
        'json': json_style,
    }
    file1 = parser(file1)
    file2 = parser(file2)
    diff_dict = diff(file1, file2)
    return format_type[output_format](diff_dict)


def diff(dict1, dict2):
    """Generate tree.

    Args:
        dict1: first_file
        dict2: second_file

    Returns:
        dict
    """
    tree = {}
    keys = dict1.keys() | dict2.keys()
    for key in sorted(keys):
        tree.update(check_tree_item(key, dict1, dict2))
    return tree


def check_tree_item(key, dict1, dict2):
    """Classifier tree items.

    Args:
        key: dict_key
        dict1: first_file
        dict2: second_file

    Returns:
        dict
    """
    deleted = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    dict1_key = dict1.get(key)
    dict2_key = dict2.get(key)
    if isinstance(dict1_key, dict) and isinstance(dict2_key, dict):
        tree_value = make_value('children', diff(dict1_key, dict2_key))
    elif key in added:
        tree_value = make_value('added', dict2_key)
    elif key in deleted:
        tree_value = make_value('deleted', dict1_key)
    elif dict1_key == dict2_key:
        tree_value = make_value('unchanged', dict1_key)
    else:
        tree_value = make_value(
            'updated',
            value_tree='',
            old=dict1_key,
            new=dict2_key,
        )
    return {key: tree_value}


def make_value(type_tree, value_tree='', old='', new=''):
    """Make tree value.

    Args:
        type_tree: name of type
        value_tree: value
        old: old value
        new: new value

    Returns:
        dict
    """
    if type_tree != 'updated':
        return {'type': type_tree, 'value': value_tree}
    return {'type': type_tree, 'old': old, 'new': new}
