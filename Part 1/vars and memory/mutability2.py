# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:25:36 2019

@author: Stefan Draghici
"""

a='hello'
b=a
print(hex(id(a)))
print(hex(id(b)))

x=[1,2,3]
y=x
print(hex(id(x)))
print(hex(id(y)))
y.append(4)
print(hex(id(x)))
print(hex(id(y)))
