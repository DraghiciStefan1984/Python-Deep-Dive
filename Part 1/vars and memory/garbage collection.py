# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 07:32:35 2019

@author: Stefan Draghici
"""

import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj)==object_id:
            return 'object exists'
    return 'not found'

class A:
    def __init__(self):
        self.b=B(self)
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))
        
class B:
    def __init__(self, a):
        self.a=a
        print('B: self: {0}, a:{1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()
my_var=A()
a_id=id(my_var)
b_id=id(my_var.b)
print(hex(a_id), hex(b_id))
print(ref_count(a_id))
print(ref_count(b_id))

my_var=None
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

gc.collect()
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))
