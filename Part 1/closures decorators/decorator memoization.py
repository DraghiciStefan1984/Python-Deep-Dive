#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:24:54 2019

@author: stefan
"""

def fib(n):
    print('calculating fib({0})'.format(n))
    return 1 if n<3 else fib(n-1)+fib(n-2)

class Fibo():
    def __init__(self):
        self.cache={1:1, 2:1}
        
    def fibo(self, n):
        if n not in self.cache:
            print('calculating fibo({0})'.format(n))
            self.cache[n]=self.fibo(n-1)+self.fibo(n-2)
        return self.cache[n]
    
f=Fibo()
print(f.fibo(10))

def fib_closure():
    cache={1:1, 2:1}
    def calc_fib(n):
        if n not in cache:
            print('calculating fib_closure({0})'.format(n))
            cache[n]=calc_fib(n-1)+calc_fib(n-2)
        return cache[n]
    return calc_fib

f=fib_closure()
f(10)

def memoize_fib_decorator(fib):
    cache=dict()
    def inner(n):
        if n not in cache:
            cache[n]=fib(n)
        return cache[n]
    return inner

@memoize_fib_decorator
def fib2(n):
    print('calculating fib({0})'.format(n))
    return 1 if n<3 else fib2(n-1)+fib2(n-2)

print(fib2(10))