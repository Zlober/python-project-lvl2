# Gendiff package

### Links

This project was built using these tools:


### Hexlet tests and linter status:
[![Actions Status](https://github.com/Zlober/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Zlober/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a0650203237396645f3c/maintainability)](https://codeclimate.com/github/Zlober/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a0650203237396645f3c/test_coverage)](https://codeclimate.com/github/Zlober/python-project-lvl2/test_coverage)

Gendiff is a CLI utility for finding differences between configuration files.

## Usage
### As external library
```python
from gendiff import generate_diff

diff = generate_diff(filepath1, filepath2)
```
### As CLI tool
```
> gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
## Comparing flat JSON files
```bash
gendiff file1.json file2.json
```

If `format` option is omitted, output will be in `stylish` by default.
[![asciicast](https://asciinema.org/a/rIfiUDF1zfFWe2kZykAs83pWn.svg)](https://asciinema.org/a/rIfiUDF1zfFWe2kZykAs83pWn)

## Comparing flat YAML files
```bash
gendiff file1.yaml file2.yaml
```
[![asciicast](https://asciinema.org/a/D6YNR8ryM2YKJrWp39jRkpnr4.svg)](https://asciinema.org/a/D6YNR8ryM2YKJrWp39jRkpnr4)

## Comparing files with nested structures

```bash
gendiff complex_file1.json complex_file2.json
```

[![asciicast](https://asciinema.org/a/UsDV53gGAr3QDbvYZAMBplZEd.svg)](https://asciinema.org/a/UsDV53gGAr3QDbvYZAMBplZEd)

## Plain text format for output

```bash
gendiff -f plain file1.json file2.json
```

[![asciicast](https://asciinema.org/a/7xKqJWCdh83zcqad04rQHE5KV.svg)](https://asciinema.org/a/7xKqJWCdh83zcqad04rQHE5KV)
