# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 08:01:23 2020

@author: Stefan Draghici
"""

a=10

def my_func1(n):
    c=n**2
    return c

def my_func2(n):
    print('global a:', a)
    c=a**n
    return c

def my_func3(n):
    a=20
    c=a**n
    return c

def my_func4(n):
    global a
    a=20
    c=a**n
    return c

def outer_func():
    x='hello'
    def inner_func():
        print(x)
    inner_func()
    
def outer_func2():
    x='hello'
    def inner_func():
        nonlocal x
        x='python'
        print('inner:', x)
    inner_func()

#test
print(my_func2(10))
print(my_func3(2))