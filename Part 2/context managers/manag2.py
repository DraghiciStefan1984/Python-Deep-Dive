# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 07:03:11 2020

@author: Stefan Draghici
"""

def my_gen():
    try:
        print('creating context')
        yield [1,2,3,4]
    finally:
        print('exit context')
        
        
class GenCtxManager:
    def __init__(self, gen_func):
        self._gen=gen_func()
        
    def __enter__(self):
        return next(self._gen)
    
    def __exit__(self, exc_type, exc_vaue, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False
  
    
def context_manager_decorator(gen_fn):
    def inner(*args, **kwargs):
        gen=gen_fn(*args, **kwargs)
        ctx=GenCtxManager(gen)
        return ctx
    return inner

    
@context_manager_decorator
def open_file(fname, mode='r'):
    print('opening file...')
    f=open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()
        
        
class GenFileManager:
    def __init__(self, gen):
        self.gen=gen
        
    def __enter__(self):
        return next(self.gen)
    
    


    
#test
with GenCtxManager(my_gen) as obj:
    print(obj)