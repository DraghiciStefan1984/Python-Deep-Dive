# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:05:58 2020

@author: Stefan Draghici
"""

import math

class Circle:
    def __init__(self, r):
        self._radius=r
        self._area=None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius=r
    
    @property
    def area(self):
        if self._area is None:
            self._area=math.pi*(self.radius**2)
        return self._area
    
    
class Factorials:
    def __iter__(self):
        return self.FactIter()
    
    class FactIter:
        def __init__(self):
            self.i=0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.i>=self.length:
                raise StopIteration
            else:
                result=math.factorial(self.i)
                self.i+=1
                return result