#!/usr/bin/env python3
""" Using union to combine int and float """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return str and Union of int or float """
    return (k, (v**2))
