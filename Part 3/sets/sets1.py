# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:53:34 2020

@author: Stefan Draghici
"""

s1={'a', 12, (45, 78), False}
s2=set([5,6,2,1,3,1])
s3=set(range(100))

d1={'a':1, 'b':2}
d2={'c':3, 'd':4}

s4=set(d1)
print(s4)

s5={c for c in 'python'}
print(s5)

sa={'a','b','c'}
sb={1,3,2}
s6={*sa, *sb}
print(s6)

s7={c for c in 'aaabbbbcchhhh'}
print(s7)

#collections comparison
from timeit import timeit

n=100_000
number=1_000
search=92156

s={i for i in range(n)}
l=[i for i in range(n)]
d={i:None for i in range(n)}

t_list=timeit(f'{search} in l', globals=globals(), number=number)
t_set=timeit(f'{search} in s', globals=globals(), number=number)
t_dict=timeit(f'{search} in d', globals=globals(), number=number)

print(t_list)
print(t_set)
print(t_dict)

print(l.__sizeof__())
print(s.__sizeof__())
print(d.__sizeof__())


#set operations
s={86,12,21,51,55,4}
print(s)

s.add(45)
print(s)

s.add(45)
print(s)

s.discard(21)
print(s)

s.pop()
print(s)
