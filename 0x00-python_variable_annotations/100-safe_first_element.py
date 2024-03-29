#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""


import typing

def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
            """ duck-typed annotation """
            if lst:
                return lst[0]
            else:
                return None
