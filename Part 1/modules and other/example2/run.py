# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:43:27 2020

@author: Stefan Draghici
"""

print(f'loading run.py:__name__={__name__}')

#import module1
import timing

code='[x**2 for x in range(1000000)]'
result=timing.timeit(code, 100)
print(result)