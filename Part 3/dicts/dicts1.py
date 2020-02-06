# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:03:18 2020

@author: Stefan Draghici
"""

import math


d={'unu':1, 'doi':2}

#d2={func:[1,2,3,4]}

def fn_add(a, b):
    return a+b

def fn_inv(a):
    return 1/a

def fn_mult(a, b):
    return a*b

funcs={fn_add:(10, 20), fn_inv:(45,), fn_mult:(13, 15)}

dict1={'a':100, 'b':{'x':1, 'y':2}, 'c':[1,2,3]}
dict2=dict(dict1)

keys=['a','b','c']
values=(1,2,3)
d1={}
for k, v in zip(keys, values):
    d1[k]=v
    
keys2='abcgdadf'
values2=range(1, 100)
d2={k:v for k, v in zip(keys2,values2) if v%2==0}

x_coords=(-2, -1, 0, 1, 2)
y_coords=(-2, -1, 0, 1, 2)
grid=[(x,y) for x in x_coords for y in y_coords]
grid_extended={(x, y, math.hypot(x, y)) for x, y in grid}

#test
for f in funcs:
    result=f(*funcs[f])
    print(result)
    
for f, args in funcs.items():
    print(f(*args))
    
print(dict1 is dict2)
print(d1)
print(d2)
print(grid)
print(grid_extended)