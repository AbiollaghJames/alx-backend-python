#!/usr/bin/env python3
""" sum list of different data types """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ return sum of type float """
    return float(sum(mxd_list))
