#!/usr/bin/env python3
"""Type annotation """

from typing import Mapping, Any, Union, TypeVar


T = TypeVar("T")

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """safeely get value from dict like object """
    if key in dct:
        return dct[key]
    else:
        return default
