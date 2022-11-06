from gendiff.formatters import convert_exception


def plain(value):
    """Return formatted values for Plain output."""
    children = []

    def inner(data, node):
        result = []
        for k, v in data.items():
            if v['type'] == 'children':
                node.append(k)
                result.append(inner(v['value'], node))
                node.pop()
            elif v['type'] == 'added':
                result.append(f"Property {'.'.join(node + [k])} was added with value: "
                              f"{check_for_complex(v['value'])}")
            elif v['type'] == 'deleted':
                result.append(f"Property {'.'.join(node + [k])} was removed")
            elif v['type'] == 'updated':
                result.append(f"Property {'.'.join(node + [k])} was updated. "
                              f"From {check_for_complex(v['old'])} to {check_for_complex(v['new'])}")
        return '\n'.join(result)
    return inner(value, children)


def check_for_complex(value):
    """Check the value for complex value"""
    if isinstance(value, dict):
        return '[complex value]'
    return convert_exception(value)
