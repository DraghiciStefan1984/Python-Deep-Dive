#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:09:49 2019

@author: stefan
"""

def log_decorator(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args, **kwargs):
        run_datetime=datetime.now(timezone.utc)
        result=fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_datetime, fn.__name__))
        return result
    return inner

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

@log_decorator
def func1():
    pass

@log_decorator
def func2():
    pass

@timer_decorator
@log_decorator
def factorial(n):
    from operator import mul
    from functools import reduce
    return reduce(mul, range(1, n+1))

factorial(3)
factorial(8)

func1()
func2()