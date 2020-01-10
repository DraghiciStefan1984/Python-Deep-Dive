# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:18:25 2020

@author: Stefan Draghici
"""

import sys
import ctypes
import gc


var=10
print(var)
print(hex(id(var)))

a=[1,2,3]
print(hex(id(a)))
print(sys.getrefcount(a))

def ref_count(address:int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

c=a

print(ref_count(id(a)))

#garbage collection

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj)==object_id:
            return 'object exists'
    return 'not found'


class A:
    def __init__(self):
        self.b=B(self)
        print('A: self - {0}, b - {1}'.format(hex(id(self)), hex(id(self.b))))
        
class B:
    def __init__(self, a):
        self.a=a
        print('B: self - {0}, a - {1}'.format(hex(id(self)), hex(id(self.a))))
        
gc.disable()

var=A()
print(hex(id(var.b)))
print(hex(id(var.b.a)))

print(object_by_id(id(var)))
gc.collect()
print(object_by_id(id(var)))
