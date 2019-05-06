#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:13:39 2019

@author: stefan
"""

def outer():
    x='python'
    def inner():
        print(x)
    return inner

fn=outer()

print(fn.__code__.co_freevars)
print(fn.__closure__)

def outer2():
    x=[1,2,3]
    print(hex(id(x)))
    def inner2():
        y=x
        print(hex(id(y)))
    return inner2        

fn2=outer2()
fn2()

def outer3():
    count=0
    def inc():
        nonlocal count
        count+=1
        return count
    return inc

fn3=outer3()