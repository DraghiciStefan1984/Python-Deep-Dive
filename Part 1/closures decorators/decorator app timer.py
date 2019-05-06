#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:04:04 2019

@author: stefan
"""

def timer_decorator(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start=perf_counter()
        result=fn(*args, **kwargs)
        end=perf_counter()
        elapsed=end-start
        arguments=[str(a) for a in args]
        keyword_arguments=['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args=arguments+keyword_arguments
        args_string=', '.join(all_args)
        print('{0}({1}) took {2:.6f} seconds to run.'.format(fn.__name__, args_string, elapsed))
        return result
    return inner


def fibo_rec(n):
    if n<=2:
        return 1
    return fibo_rec(n-1)+fibo_rec(n-2)

@timer_decorator
def fibo_iter(n):
    fibo1=1
    fibo2=1
    for i in range(3, n+1):
        fibo1, fibo2=fibo2, fibo1+fibo2
    return fibo2

@timer_decorator
def call_fibo_rec(n):
    return fibo_rec(n)

@timer_decorator
def fibo_reduce(n):
    from functools import reduce
    initial=(1, 0)
    dummy=range(n)
    fib_n=reduce(lambda prev, n: (prev[0]+prev[1], prev[0]), dummy, initial)
    return fib_n[0]

call_fibo_rec(10)
fibo_iter(10)
fibo_reduce(10)