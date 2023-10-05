#!/usr/bin/env python3
""" Duck type an iterable object """

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list of tuple of sequence and int """
    return [(i, len(i)) for i in list]
