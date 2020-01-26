# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:40:38 2020

@author: Stefan Draghici
"""

from copy import deepcopy


l1=[1,2,3]

l2=[]

for item in l1:
    l2.append(item)
print(l2)
print(id(l1), id(l2))


l2=l1.copy()
print(l2)
print(id(l1), id(l2))


v1=[0,0]
v2=[0,0]
line1=[v1, v2]
line2=line1.copy()
print(id(line1), id(line2))
print(id(line1[0]), id(line2[0]))

line2=deepcopy(line1)
print(id(line1), id(line2))
print(id(line1[0]), id(line2[0]))