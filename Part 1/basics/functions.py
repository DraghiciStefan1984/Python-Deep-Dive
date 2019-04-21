# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:05:02 2019

@author: Stefan Draghici
"""

def func1():
    print('standard function')
    
def func2(a, b):
    return a+b

#a function using annotation to specify the type of the atributes
def func3(a:float, b:float):
    return a*b

def func4():
    return func5()

def func5():
    print('running func5 from func4')
    
#assign a function to a variable, call with ()
var_func=func1

#lambda assigned to a variable, call with ()
l=lambda x:x*2