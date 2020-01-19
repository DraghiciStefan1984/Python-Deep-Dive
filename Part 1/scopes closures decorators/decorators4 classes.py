# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:04:29 2020

@author: Stefan Draghici
"""

#class decorator
class MyClass:
    def __init__(self, a, b):
        self.a=a
        self.b=b
        
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('called a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass(23, 67)
def func(s):
    print('hello {0}'.format(s))        
        
#test
func('world')