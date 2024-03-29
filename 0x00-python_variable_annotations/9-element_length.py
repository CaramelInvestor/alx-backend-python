#!/usr/bin/env python3

"""Annotate the below functions parameters and
return values with the appropriate types
    def element_length(lst):
        return [(i, len(i)) for i in lst]"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """this function returns the number of elements"""
    return [(i, len(i)) for i in lst]
