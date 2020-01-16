# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:05:33 2020

@author: Stefan Draghici
"""

from functools import reduce


l=[4,7,8,9,4,1,3]

_max=lambda x, y: x if x>y else y

def max_sequence(sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=_max(result, x)
    return result


s={True, 1, 0, None}


#test
print(max_sequence(l))
print(reduce(_max, l))
print(all(s))
print(any(s))