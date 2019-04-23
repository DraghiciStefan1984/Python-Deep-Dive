# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:50:41 2019

@author: Stefan Draghici
"""

a='hello'
b='hello'
print(id(a), id(b))

a='hello world'
b='hello world'
print(id(a), id(b))
print(a==b)
print(a is b)