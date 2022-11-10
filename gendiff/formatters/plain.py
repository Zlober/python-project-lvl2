"""Output in plain style."""
from gendiff.formatters.stylish import convert_exception


def plain(tree, parent=''):
    """Return formatted values for Plain output.

    Args:
        tree: dict
        parent: current parent

    Returns:
        string in style
    """
    style = []
    for key, tree_item in tree.items():
        node = get_parent(parent, key)
        tree_type = tree_item.get('type')
        if tree_type == 'children':
            style.append(plain(tree_item.get('value'), node))
        elif tree_type != 'unchanged':
            style.append(make_property(tree_type, node, tree_item))
    return '\n'.join(style)


def get_parent(parent, node):
    """Get parent value.

    Args:
        parent: current parent
        node: children

    Returns:
        path with root
    """
    if not parent:
        return node
    return '{parent}.{node}'.format(parent=parent, node=node)


def make_property(tree_type, node, tree_item):
    """Make property text.

    Args:
        tree_type: type of tree
        node: path
        tree_item: value of tree

    Returns:
        string in format
    """
    tree_items = {
        'added': "Property '{node}' was added with value: {tree_value}".format(
            node=node,
            tree_value=check_for_complex(tree_item.get('value')),
        ),
        'deleted': "Property '{node}' was removed".format(node=node),
        'updated': "Property '{node}' was updated. From {old} to {new}".format(
            node=node,
            old=check_for_complex(tree_item.get('old')),
            new=check_for_complex(tree_item.get('new')),
        ),
    }
    return tree_items.get(tree_type)


def check_for_complex(tree_value):
    """Check the value for complex value.

    Args:
        tree_value: value

    Returns:
        complex or unchanged
    """
    if isinstance(tree_value, dict):
        return '[complex value]'
    return convert_exception(tree_value)
