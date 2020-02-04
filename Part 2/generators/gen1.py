# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:42:06 2020

@author: Stefan Draghici
"""

import math

class FactIter:
    def __init__(self, n):
        self.n=n
        self.i=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        else:
            result=math.factorial(self.i)
            self.i+=1
            return result
        
        
def fib_rec(n):
    if n<=1:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)
    
    
def fib(n):
    fib0=1
    fib1=0
    for i in range(n-1):
        fib0, fib1=fib1, fib0+fib1
        yield fib1
    #return fib1
    
    
#iter from gen
def squares_gen(n):
    for i in range(n):
        yield i**2
        
class Squares:
    def __init__(self, n):
        self.n=n
        
    def __iter__(self):
        return Squares.__squares_gen(self.n)
    
    @staticmethod
    def __squares_gen(n):
        for i in range(n):
            yield i**2
        
        
#test
fact_iter=FactIter(5)
print(list(fact_iter))
print([fib_rec(i) for i in range(10)])

sq=Squares(10)
print(list(sq))








