"""Expected results constants."""

SIMPLE_STRING = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

SIMPLE_PLAIN = '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''

SIMPLE_JSON = '''{
    "follow": {
        "type": "deleted",
        "value": false
    },
    "host": {
        "type": "unchanged",
        "value": "hexlet.io"
    },
    "proxy": {
        "type": "deleted",
        "value": "123.234.53.22"
    },
    "timeout": {
        "type": "updated",
        "old": 50,
        "new": 20
    },
    "verbose": {
        "type": "added",
        "value": true
    }
}'''

COMPLEX_STRING = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

COMPLEX_PLAIN = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: blah blah
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From  to so much
Property 'common.setting6.ops' was added with value: vops
Property 'group1.baz' was updated. From bas to bars
Property 'group1.nest' was updated. From [complex value] to str
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

COMPLEX_JSON = '''{
    "common": {
        "type": "children",
        "value": {
            "follow": {
                "type": "added",
                "value": false
            },
            "setting1": {
                "type": "unchanged",
                "value": "Value 1"
            },
            "setting2": {
                "type": "deleted",
                "value": 200
            },
            "setting3": {
                "type": "updated",
                "old": true,
                "new": null
            },
            "setting4": {
                "type": "added",
                "value": "blah blah"
            },
            "setting5": {
                "type": "added",
                "value": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "type": "children",
                "value": {
                    "doge": {
                        "type": "children",
                        "value": {
                            "wow": {
                                "type": "updated",
                                "old": "",
                                "new": "so much"
                            }
                        }
                    },
                    "key": {
                        "type": "unchanged",
                        "value": "value"
                    },
                    "ops": {
                        "type": "added",
                        "value": "vops"
                    }
                }
            }
        }
    },
    "group1": {
        "type": "children",
        "value": {
            "baz": {
                "type": "updated",
                "old": "bas",
                "new": "bars"
            },
            "foo": {
                "type": "unchanged",
                "value": "bar"
            },
            "nest": {
                "type": "updated",
                "old": {
                    "key": "value"
                },
                "new": "str"
            }
        }
    },
    "group2": {
        "type": "deleted",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "type": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}'''