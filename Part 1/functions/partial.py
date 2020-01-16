# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:09:02 2020

@author: Stefan Draghici
"""

from functools import partial


def my_func(a, b, c):
    print(a, b, c)
    
def f(x, y):
    return my_func(10, x, y)

f1=partial(my_func, 10)

def my_func1(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)
    
def f1(x, *args, kw, **kwargs):
    return my_func1(10, x, *args, k1='a', k2=kw, **kwargs)

#test
f(20, 35)
f1(30, 45)