# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:12:54 2020

@author: Stefan Draghici
"""


#counter decorator
def counter(fn):
    count=0
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print('function {0} was called {1} times.'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

@counter
def add(a, b):
    """
    adds two numbers
    """
    return a+b


#timer decorator
def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start=perf_counter()
        result=fn(*args, **kwargs)
        end=perf_counter()
        elapsed=end-start
        _args=[str(a) for a in args]
        _kwargs=['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args=_args+_kwargs
        all_args=','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, all_args, elapsed))
        return result
    
    return inner


@timed
def fibo_rec(n):
    if n<=2:
        return 1
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)
    
@timed
def fibo_loop(n):
    fib1=1
    fib2=1
    for i in range(3, n+1):
        fib1, fib2=fib2, fib1+fib2
        
@timed
def fibo_reduced(n):
    from functools import reduce
    initial=(1, 0)
    dummy=range(n)
    fib_n=reduce(lambda prev, n: (prev[0]+prev[1], prev[0]), dummy, initial)
    return fib_n[0]


#test
add(10, 20)
add(10, 30)
fibo_rec(2)
fibo_rec(5)
fibo_rec(10)
fibo_loop(2)
fibo_loop(5)
fibo_loop(10)
fibo_reduced(2)
fibo_reduced(5)
fibo_reduced(10)