# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:03:43 2019

@author: Stefan Draghici
"""

def positional(a, b, c=0, d=0):
    return a+b+c+d

print(positional(2, 3))
print(positional(2, 3, 4))
print(positional(2, 3, 4, 5))
print()

def func_args(a, b, *args):
    print(a)
    print(b)
    print(args)
    
func_args('a', 'b')
func_args('x', 'y', [1,2,3])
func_args(10,20,30,40,50)
print()

def avg(*args):
    if len(args)==0:
        return 0
    return sum(args)/len(args)

print('avg is {}'.format(avg(2, 3)))
print('avg is {}'.format(avg(2, 3, 4, 5)))
print('avg is {}'.format(avg(2, 3, 20, 4, 78, 8)))
print()

def func_kwargs(**kwargs):
    print(kwargs)
    
func_kwargs()
func_kwargs(a=2, b=4)

def func_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    
func_args_kwargs(1,2,3, a=10, b=20, c=False, d=('a','b','c'))