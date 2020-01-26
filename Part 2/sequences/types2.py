# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 08:53:18 2020

@author: Stefan Draghici
"""

l=[4,8,1,5,3]
print(l)

l[0]=15
print(l)

l[0:2]=('a', 'b', 'c', 'd')
print(l)

l.append([8,9])
print(l)

l.extend([10, 11])
print(l)

del l[2]
print(l)

l.insert(5, 'x')
print(l)

#in place reversal
print(l[::-1])