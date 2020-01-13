# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:38:43 2020

@author: Stefan Draghici
"""

import time


def func1(a, b, *args):
    print(a, b, args)
    
def func2(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)
    
def time_it(fn, *args, rep=1, **kwargs):
    start=time.perf_counter()
    for i in range(rep):
        fn(args, kwargs)
    end=time.perf_counter()
    return (end-start)/rep

def compute_powers_1(n, *, start=1, end):
    results=[]
    for i in range(start, end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1, end):
    return [n**i for i in range(start, end)]

def compute_powers_3(n, *, start=1, end):
    #using generator expression
    return (n**i for i in range(start, end))
    
#test
func1(1, 2, 'a', 'b', 3, 5)
func2(1, 2, 'a', 'b', 3, 5, 'a', c=True, d=1)
time_it(print, 1, 2, 3, sep='-', end='**\n', rep=5)