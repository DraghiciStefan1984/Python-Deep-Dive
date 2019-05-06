#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:35:36 2019

@author: stefan
"""

print(callable(print))
result=print('hello')
print(result)
print()

#other higher order functions

#map
def fact(n):
    return 1 if n<2 else n*fact(n-1)

print(fact(5))
print(fact(8))
print(fact(13))
print()

#results=map(fact, range(8))
#for r in results:
#    print(r)
results=list(map(fact, range(8)))
print(results)

l1=[1,2,3,4,5]
l2=[34, 56, 78]
l3=88, 89, 90, 56, 76
results=list(map(lambda x, y, z: x+y+z, l1, l2, l3))
print(results)

#filter
result=list(filter(lambda x:x%3==0, range(20)))
print(result)

#zip
l1=[3,4,6,5,4]
l2=[58,97,67]
l3='python'
result=list(zip(l1, l2, l3))
print(result)

print(list(zip(range(1000), 'python')))

fact_list=[fact(n) for n in range(10)]
print(fact_list)

fact_gen=list((fact(n) for n in range(10)))
print(fact_gen)

rez=[x+y for x, y in zip(l1, l2)]
print(rez)
