#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:04:26 2019

@author: stefan
"""

def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('decorated func called: a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print('Hello {}'.format(s))
    
my_func('dumbass.')


class MyClass:
    def __init__(self, a, b):
        self.a=a
        self.b=b
        
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('decorated func called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner
    
        
obj=MyClass(33, 88)
obj.__call__(100)


@MyClass(10, 20)
def my_func2(s):
    print('Hello {}'.format(s))
    
my_func2('genius.')
