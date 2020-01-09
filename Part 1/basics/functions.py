# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:50:53 2020

@author: Stefan Draghici
"""


def func1():
    print('func 1')
    
    
# :int is just a convention, the compiler will ignore it
def func2(a:int, b:int):
    return a+b


def func3():
    return func4()


def func4():
    return 'func 4'


fn1=lambda x: x*2


#test
print(func2('a', 'c'))
print(func2([3,2,5], [3]))
print(func3())
print(fn1(3))