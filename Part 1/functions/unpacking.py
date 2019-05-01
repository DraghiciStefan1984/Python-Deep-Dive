# -*- coding: utf-8 -*-
"""
Created on Wed May  1 09:52:57 2019

@author: Stefan Draghici
"""

t1=1,
t2=(1,)
print(t1)

a, b, c=[1,2,3]
print(a)
print(b)
print(c)
print()

a, b, *c=[1,2,3,4,5,6]
print(a)
print(b)
print(c)
print()

a, *b, c={1,2,3,4,5}
print(a)
print(b)
print(c)
print()

d={'a':1, 'b':2, 'c':3, 'd':4}
a, b, c, d=d
print(a)
print(b)
print(c)
print(d)
print()

a, *b, c, d='python'
print(a)
print(b)
print(c)
print(d)
print()

l1=[1,2,3]
l2=[4,5,6]
l3=[l1, l2]
print(l3)
l3=[*l1, *l2]
print(l3)
print()