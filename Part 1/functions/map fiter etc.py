# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 07:27:38 2020

@author: Stefan Draghici
"""


def fact(n):
    return 1 if n<2 else n*fact(n-1)

l1=[4,6,5]
l2=[7,8,4,1]
l3=[2,3]

#test
print(list(map(fact, range(6))))
print(list(map(lambda x, y:x+y, l1, l2)))
print(list(zip(l1, l2, l3)))
print(list(zip(range(10000), 'python')))