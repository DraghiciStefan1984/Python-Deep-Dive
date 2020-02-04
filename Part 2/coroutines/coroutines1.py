# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:39:58 2020

@author: Stefan Draghici
"""

from collections import deque


def produce(dq, n):
    for i in range(1, n):
        dq.appendleft(i)
        if len(dq)==dq.maxlen:
            print('queue full - yelding control')
            yield
        
        
def consume(dq):
    while True:
        while len(dq)>0:
            print('proessing: ', dq.pop())
        print('queue empty - yielding control')
        yield
        
        
def coordinator():
    dq=deque(maxlen=50)
    producer=produce(dq, 40)
    consumer=consume(dq)
    while True:
        try:
            print('producing...')
            next(producer)
        except StopIteration:
            break
        finally:
            print('consuming...')
            next(consumer)
    

#test
coordinator()