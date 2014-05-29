#!usr/bin/env python
import yaml


def parse_comm(func):
    doc = yaml.load(func.__doc__)
    return doc


if __name__ == '__main__':
    import continuous
    for attr in dir(continuous):
        if not attr.startswith('_'):
            func = getattr(continuous, attr)
            parse_comm(func)