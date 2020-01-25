# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:47:53 2020

@author: Stefan Draghici
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing=namedtuple('Timing', 'repeats elapsed averages')

def timeit(code, repeats=10):
    code=compile(code, filename='<string>', mode='exec')
    start=perf_counter()
    for _ in range(repeats):
        exec(code)
    end=perf_counter()
    elapsed=end-start
    average=elapsed/repeats
    return Timing(repeats, elapsed, average)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help='python snippet')
    parser.add_argument('-r', '--repeats', type=int, default=10)