# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:14:48 2020

@author: Stefan Draghici
"""

from math import factorial


squares=[i**2 for i in range(1, 101) if i%2==0]

table=[[i*j for j in range(1, 11)] for i in range(1, 11)]

def combo(n, k):
    return factorial(n)//(factorial(n)*factorial(n-k))

size=10
pascal=[[combo(n, k) for k in range(n+1)] for n in range(size+1)]

l1=['a','b','c']
l2=['x','y','z']

list_comp=[s1+s2 for s1 in l1 for s2 in l2]

l3=[1,2,3,4,5,6,7,8,9]
l4=['a','b','c','d']

list_comp_2=[(item1, item2) for index1, item1 in enumerate(l3) for index2, item2 in enumerate(l4) if index1==index2]

#test
print(squares)
print(table)
print(pascal)
print(list_comp)
print(list_comp_2)