#!/usr/bin/env python3
""" Callable to create complex function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a Callable function """
    def multiplier_func(x: float) -> float:
        """ return x multiplied by multiplier """
        return x * multiplier

    return multiplier_func
