# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:56:37 2020

@author: Stefan Draghici
"""

a=(10,20,30)
b=40,50,60

def print_tuple(t):
    for e in t:
        print(a)
        
a=1,2,3,4,5,6
x,*_,y,z=a
print(x, y, z)


class Point2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'
    
    
################ named tuples ###############
from collections import namedtuple

Point2D=namedtuple('Point2D', ['x', 'y'])

#test
p1=Point2D(10, 20)
p2=Point2D(13, 18)