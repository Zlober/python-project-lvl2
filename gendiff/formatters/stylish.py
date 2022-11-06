from itertools import chain
import json


def stylish(data, spacer_count=4):
    """Stylish tree"""
    result = []
    spacer = ' '
    for k, v in data.items():
        if v['type'] == 'added':
            indent = spacer * (spacer_count - 2)
            v = convert_exception(unpack(v['value'], spacer_count))
            result.append(f'{indent}+ {k}: {v}')
        elif v['type'] == 'updated':
            indent = spacer * (spacer_count - 2)
            old = convert_exception(unpack(v['old'], spacer_count))
            result.append(f'{indent}- {k}: {old}')
            new = convert_exception(unpack(v['new'], spacer_count))
            result.append(f'{indent}+ {k}: {new}')
        elif v['type'] == 'deleted':
            indent = spacer * (spacer_count - 2)
            v = convert_exception(unpack(v['value'], spacer_count))
            result.append(f'{indent}- {k}: {v}')
        elif v['type'] == 'children':
            indent = spacer * spacer_count
            val = stylish(v["value"], spacer_count + 4)
            result.append(f'{indent}{k}: {val}')
        else:
            indent = spacer * spacer_count
            v = convert_exception(unpack(v['value'], spacer_count))
            result.append(f'{indent}{k}: {v}')
    result = chain('{', result, [spacer * (spacer_count - 4) + '}'])
    return '\n'.join(result)


def unpack(data, spacer_count):
    """Unpack children"""
    spacer = ' '
    result = []
    if not isinstance(data, dict):
        return data
    for k, v in data.items():
        if isinstance(v, dict):
            v = unpack(v, spacer_count + 4)
        result.append(f'{spacer * (spacer_count + 4)}{k}: {v}')
    result = chain('{', result, [spacer * spacer_count + '}'])
    return '\n'.join(result)


def convert_exception(value):
    """Return JSON representation of a Python object."""
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value
