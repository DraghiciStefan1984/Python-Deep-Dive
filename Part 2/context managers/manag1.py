# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:56:06 2020

@author: Stefan Draghici
"""

def test():
    with open('test.txt', 'w') as file:
        print('inside with: file closed', file.closed)
        return file


class ContextManager:
    def __init__(self):
        self.obj=None
        
    def __enter__(self):
        print('entering context...')
        self.obj='the return object'
        return self.obj
    
    def __exit__(self, exec_type, exec_value, exect_tb):
        print('exiting context...')
        if exec_type:
            print(f'***error occured: {exec_type}:{exec_value}')
        return False
    
    
class File:
    def __init__(self, name, mode):
        self.name=name
        self.mode=mode
        
    def __enter__(self):
        print('opening file')
        self.file=open(self.name, self.mode)
        return self
    
    def __exit__(self, exec_type, exec_value, exect_tb):
        print('closing file')
        self.file.close()
        return False
 
    
#test
file=test()

'''
with ContextManager() as obj:
    print('inside context')
    raise ValueError('custom mesg')
'''
    
with File('test.txt', 'r') as file_ctx:
    print(next(file_ctx))
    print(file_ctx.name)
    print(file_ctx.mode)