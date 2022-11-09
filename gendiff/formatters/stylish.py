"""Output in stylish style."""
import json
from itertools import chain


def stylish(tree, spacer_count=4):
    """Format in Stylish tree style.

    Args:
        tree: dict
        spacer_count: count of spacer

    Returns:
        string in style
    """
    style = []
    for key, tree_item in tree.items():
        tree_type = tree_item.get('type')
        tree_value = tree_item.get('value')
        if tree_type == 'children':
            style.append('{indent}{key}: {tree_value}'.format(
                indent=make_indent(spacer_count, tree_type),
                key=key,
                tree_value=stylish(tree_value, spacer_count + 4),
            ))
        elif tree_type == 'updated':
            style.append('{indent}{key}: {old}'.format(
                indent=make_indent(spacer_count, 'old'),
                key=key,
                old=convert_exception(unpack(tree_item['old'], spacer_count)),
            ))
            style.append('{indent}{key}: {new}'.format(
                indent=make_indent(spacer_count, 'new'),
                key=key,
                new=convert_exception(unpack(tree_item['new'], spacer_count)),
            ))
        else:
            style.append('{indent}{key}: {tree_value}'.format(
                indent=make_indent(spacer_count, tree_type),
                key=key,
                tree_value=convert_exception(unpack(tree_value, spacer_count)),
            ))
    style = chain('{', style, ['{indent}{block_end}'.format(
        indent=' ' * (spacer_count - 4),
        block_end='}',
    )])
    return '\n'.join(style)


def make_indent(spacer_count, item_type):
    """Make indent.

    Args:
        spacer_count: count of space
        item_type: type of tree

    Returns:
        string indent block
    """
    items_type = {
        'added': '+ ',
        'deleted': '- ',
        'unchanged': '',
        'old': '- ',
        'new': '+ ',
        'children': '',
    }
    return '{indent}{items_type}'.format(
        indent=' ' * (spacer_count - len(items_type[item_type])),
        items_type=items_type[item_type],
    )


def unpack(tree, spacer_count):
    """Unpack children in tree.

    Args:
        tree: dict
        spacer_count: count of spacer

    Returns:
        string in style
    """
    spacer = ' '
    children = []
    if not isinstance(tree, dict):
        return tree
    for key, tree_value in tree.items():
        if isinstance(tree_value, dict):
            tree_value = unpack(tree_value, spacer_count + 4)
        children.append('{indent}{key}: {tree_value}'.format(
            indent=spacer * (spacer_count + 4),
            key=key,
            tree_value=tree_value,
        ))
    children = chain('{', children, ['{indent}{block_end}'.format(
        indent=spacer * spacer_count,
        block_end='}',
    )])
    return '\n'.join(children)


def convert_exception(except_value):
    """Return JSON representation of a Python object.

    Args:
        except_value: item

    Returns:
        string in json style
    """
    if isinstance(except_value, bool) or except_value is None:
        return json.dumps(except_value)
    return except_value
