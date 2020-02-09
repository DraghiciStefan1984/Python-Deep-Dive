# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:51:01 2020

@author: Stefan Draghici
"""

#set operations part 2
s1={1,2,3,4}
s2={3,4,5,6}
print(id(s1), id(s2))

s1=s1&s2
print(s1)
print(id(s1))


s1={1,2,3,4}
s2={3,4,5,6}
print(id(s1), id(s2))

s1=s1|s2
print(s1)
print(id(s1))


s1={1,2,3,4}
s2={3,4,5,6}
print(id(s1), id(s2))

s1^=s2
print(s1)
print(id(s1))

#frozen sets
s1=frozenset('ddsfgfghf')
print(s1)
print(type(s1))