#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:31:12 2019

@author: stefan
"""

def func(a:'annotation for a', b: 'annotation for b with default value'=1) \
-> 'return value can be added':
    """
    documentation must be on the first line of code 
    under the function declaration. this will get compiled.
    """
    return a*b

print(help(func))
print(func.__doc__)