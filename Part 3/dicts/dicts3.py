# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:14:07 2020

@author: Stefan Draghici
"""

from copy import deepcopy

#updating, copyig, merging

d={'a':2, 'b':45, 'c':80}
d['a']=20
print(d)

d1={'a':89, 'b':12}
d2={'c':25, 'd':87}
d1.update(d2)
print(d1)

d1.update(a=30, c=55)
print(d1)

d1.update(x=47, c=45, b=88)
print(d1)

l1=[1,2,3]
l2='abc'
l3=(*l1, *l2)
print(l3)

d1={'a':89, 'b':12}
d2={'c':25, 'd':87}
d3={**d1, **d2}
print(d3)

d1={'a':[1,2], 'b':[3,4], 'c':[5,6]}

#shallow copy
d2=d1.copy()
print(d2)
print(d1 is d2)
print(d1['a'] is d2['a'])

#deep copy
d2=deepcopy(d1)
print(d1['a'] is d2['a'])
