# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:59:11 2019

@author: Stefan Draghici
"""
import sys
import ctypes

int_var=10
print(int_var)
print('address of int_var is: {0}'.format(id(int_var)))
print('hex address of int_var is: {0}'.format(hex(id(int_var))))

a=[1,2,3]
print(id(a))
print(sys.getrefcount(a))

#display the correct number of references
def ref_count(address:int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))