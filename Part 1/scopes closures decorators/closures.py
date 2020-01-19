# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 07:09:41 2020

@author: Stefan Draghici
"""

class Averager:
    def __init__(self):
        self.numbers=[]
        
    def add(self, number):
        self.numbers.append(number)
        total=sum(self.numbers)
        count=len(self.numbers)
        return total/count
    
    
#same thing, but with a closure
def averager():
    numbers=[]
    def add(number):
        numbers.append(number)
        total=sum(numbers)
        count=len(numbers)
        return total/count
    return add