# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:51:01 2019

@author: Stefan Draghici
"""

import time

def time_it(func, *args, reps=1, **kwargs):
    start=time.perf_counter()
    for i in range(reps):
        func(*args, **kwargs)
    end=time.perf_counter()
    return (end-start)/reps
    
print(time_it(print, 1,2,3,4, sep=' - ', end=' ***\n'))