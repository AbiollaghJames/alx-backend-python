#!/usr/bin/env python3
""" Callable to create complex function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], floait]:
    """ returns a function, output is Callable """
    def multiplier_func(x: float) -> float:
        """ return x multiplie by multiplier """
        return x * multiplier

    return multiplier_func
