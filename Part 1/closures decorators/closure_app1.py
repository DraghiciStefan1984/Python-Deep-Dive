#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:28:53 2019

@author: stefan
"""

class Averager:
    def __init__(self):
        self.numbers=[]
        
    def add(self, number):
        self.numbers.append(number)
        return sum(self.numbers)/len(self.numbers)
    
a=Averager()
print(a.add(20))
print(a.add(30))

def averager():
    numbers=[]
    def add(number):
        numbers.append(number)
        return sum(numbers)/len(numbers)
    return add

a=averager()
print(a(10))
print(a(30))