#!/usr/bin/env python3
"""
Complex types - mixed list
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """ will return the sum of the list as a float """
    return float(sum(mxd_lst))
