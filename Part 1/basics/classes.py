# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:54:50 2020

@author: Stefan Draghici
"""

class Rectangle:
    def __init__(self, width, height):
        self.__width=width
        self.__height=height
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if width<0:
            raise('value must be positive')
        self.__width=width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if height<0:
            raise('value must be positive')
        self.__height=height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)
    
    def __str__(self):
        return 'Rectangle: width-{0}, height-{1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle: width-{0}, height-{1}'.format(self.width, self.height)
    
    def __eq__(self, other):
        return self.width==other.width and self.height==other.height
    
    
#test
r1=Rectangle(23, 25)
print(r1.area())
print(r1.perimeter())