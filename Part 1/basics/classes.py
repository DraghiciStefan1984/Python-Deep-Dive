# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:00:29 2019

@author: Stefan Draghici
"""

class Rectangle:
    def __init__(self, width, height):
        self._width=width
        self._height=height
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width<=0:
            raise ValueError('value must be positive')
        else:
            self._width=width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def set_height(self, height):
        if height<=0:
            raise ValueError('value must be positive')
        else:
            self.height=height
        
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*self.width+2*self.height
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    #similar to __str__ butcan be called without str(obj)
    def __repr__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width==other.width and self.height==other.height
        else:
            return False
        
r1=Rectangle(10, 20)
print(r1.width, r1.height)
print(r1.area())
print(str(r1))
print(r1)