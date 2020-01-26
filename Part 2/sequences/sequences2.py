# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:37:17 2020

@author: Stefan Draghici
"""

from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    
class Line:
    def __init__(self, p1, p2):
        self.p1=p1
        self.p2=p2
        
    def __repr__(self):
        return f'Line[{self.p1.__repr__()}, {self.p2.__repr__()}]'
    
    
class CustomSequence:
    def __init__(self, n):
        self.n=n
        
    def __len__(self):
        print('called __len__')
        return self.n
    
    def __getitem__(self, value):
        if value<0 or value>=self.n:
            raise IndexError
        else:
            return 'the element'
        
        
class Fib:
    from functools import lru_cache
    def __init__(self, n):
        self.n=n
        
    def __len__(self):
        return self.n
    
    def __getitem__(self, s):
        if isinstance(s, int):
            if s<0:
                s=self.n+s
            if s<0 or s>=self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            start, stop, step=s.indeces(self.n)
            rng=range(start, stop, step)
            return [Fib._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2**10)
    def _fib(n):
        if n<2:
            return 1
        else:
            return Fib._fib(n-1)+Fib._fib(n-2)
                
    
    
#test
p1=Point(0,0)
p2=Point(10,10)
l1=Line(p1, p2)
print(p1, p2)
print(l1)

l2=deepcopy(l1)
print(id(l1), id(l2))
print(id(l1.p1), id(l2.p1))

cs=CustomSequence(32)
print(len(cs))

fib=Fib(30)
print(list(fib))








