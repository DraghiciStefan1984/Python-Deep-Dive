# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:06:59 2020

@author: Stefan Draghici
"""

def func1(a, b, *c):
    print(a)
    print(b)
    print(c)
    

func1(10, 20)
print('***********')
func1(89, 'v', 'e') 
print('***********')
func1(0, 0, 78, 78, 56, 23)


def avg(*args):
    return sum(args)/len(args)

print(avg(12, 45))
print(avg(12, 78, 95, 23))


def func2(a, b=2, c=4):
    print(a, b, c)
    
func2(23)
func2(78, 12, 45)
func2(12, b='c')


def func3(**kwargs):
    print(kwargs)
    
func3(a=1, b=3, c='c')


def func4(*args, **kwargs):
    print(args)
    print(kwargs)
    
func4(1,5,3, c=8, g='g')