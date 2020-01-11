# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:37:20 2020

@author: Stefan Draghici
"""


#tuples
a=(1,2,3)
b=1,2,3
c=tuple([4,5,6])
d=1,

a, b, c=10, {1, 2}, ['a','b']

#swap values
a, b=10, 20
print(a, b)
a, b=b, a
print(a, b)

#extended unpacking
l=[1,3,2,4]
a, b=l[0], l[1:]
print(a)
print(b)
a, *b=l
print(a)
print(b)
s='python'
a, *b=s
print(a)
print(b)
t=('a', 'b', 'c')
a, *b=t
print(a)
print(b)
[a, b, c]='xyz'
a, b, *c='python'
a, b, *c, d='python'


l1=[4,5,6]
l2=[7,8,9]
l=[*l1, *l2]
print(l)

s='abc'
l=[*l1, *s]
print(l)

s={18,1,5,'b'}
a, b, c, d=s
print(a, b, c, d)
*c,=s
print(c)

s1={'a','b','c'}
s2={7,8,9}
c={*s1, *s2}
print(c)


d1={'unu':1, 'doi':2}
d2={'trei':3, 'patru':4}

