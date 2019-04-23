# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:29:36 2019

@author: Stefan Draghici
"""

a=10
b=10
print(hex(id(a)))
print(hex(id(b)))
print('a is b: ', a is b)
print('a == b: ', a == b)

x=800
y=800
print(hex(id(x)))
print(hex(id(y)))
print('x is y: ', x is y)
print('x == y: ', x == y)

m=[1,2,3]
n=[1,2,3]
print(hex(id(m)))
print(hex(id(n)))
print('m is n: ', m is n)
print('m == n: ', m == n)