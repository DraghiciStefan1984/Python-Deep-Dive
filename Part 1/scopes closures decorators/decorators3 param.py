# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:44:23 2020

@author: Stefan Draghici
"""

from time import perf_counter


def timed(fn, reps):
    def inner(*args, **kwargs):
        total_time=0
        for i in range(reps):
            start=perf_counter()
            result=fn(*args, **kwargs)
            end=perf_counter()
            total_time+=(end-start)
        print('avg run time:{0}, reps:{1}'.format(total_time/reps, reps))
        return result
    return inner

def calc_fib(n):
    return 1 if n<3 else calc_fib(n-2)+calc_fib(n-1)

fib=timed(calc_fib, 10)

'''
@timed
def fib(n):
    return calc_fib(n)
'''

#test
fib(20)