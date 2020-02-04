# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:37:10 2020

@author: Stefan Draghici
"""

#generator expressions vs list comp
l=[i**2 for i in range(10)]
g=(i**2 for i in range(10))

start=1
stop=100
mult_list=[[i*j for j in range(start, stop+1)] for i in range(start, stop+1)]
mult_gen=((i*j for j in range(start, stop+1)) for i in range(start, stop+1))

#yield from
def matrix(n):
    gen=((i*j for j in range(1, n+1)) for i in range(1, n+1))
    return gen

def matrix_iterator(n):
    for row in matrix(n):
        yield from row

#test
print(type(l))
print(type(g))

print([list(row) for row in mult_gen])