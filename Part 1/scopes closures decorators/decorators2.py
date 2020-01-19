# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:16:19 2020

@author: Stefan Draghici
"""

from functools import wraps, reduce
from datetime import datetime, timezone
from operator import mul


#logging decorator
def logged(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt=datetime.now(timezone.utc)
        result=fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result
    return inner

#counter decorator
def counter(fn):
    count=0
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print('function {0} was called {1} times.'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

#memoize fibo decorator
def memoize(fn):
    cache=dict()
    def inner(n):
        if n not in cache:
            cache[n]=fn(n)
        return cache[n]
    return inner


@logged
def f1():
    pass

@logged
def f2():
    pass

@counter
@logged
def fact(n):
    return reduce(mul, range(1, n+1))

@memoize
def fib(n):
    print('calculating fib({})'.format(n))
    return 1 if n<3 else fib(n-1)+fib(n-2)


#test
f1()
f1()
f1()
f2()
f1()
f2()
f2()
f2()
fact(20)
fib(10)