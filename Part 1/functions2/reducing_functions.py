#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:15:43 2019

@author: stefan
"""

l=[3,6,3,2,7,4,2,3,4,7,2]

_max=lambda x, y: x if x>y else y

def max_sequence(sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=_max(result, x)
    return result

_min=lambda x, y: x if x<y else y

def min_sequence(sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=_min(result, x)
    return result

def _reduce(func, sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=func(result, x)
    return result

print(max_sequence(l))
print(_reduce(_min, l))