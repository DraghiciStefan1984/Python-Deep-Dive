#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:31:12 2019

@author: stefan
"""

mult=lambda x:x*x
add=lambda x, y:x+y
f=lambda x, *args, y, **kwargs:(x, args, y, kwargs)

def apply_func(arg, func):
    return func(arg)

print(mult(4))
print(add(7, 8))
print(f('a', 2, 3, y='y', a=1, b=8))
print(apply_func(45, mult))

#lambda for sorting
l=['a','t','u','V','E','O']
print(sorted(l, key=lambda s:s.upper()))

d={'def':300, 'ghi':450, 'jkl':200}
print(sorted(d))
print(sorted(d, key=lambda e:d[e])) 