# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:51:44 2020

@author: Stefan Draghici
"""

from math import pi
from numbers import Real


class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    def work(self):
        result=super().work()
        return f'Student works... and {result}'
    
class PythonStudent(Student):
    def work(self):
        result=super().work()
        return f'Python student codes... and {result}'
    
#########################################
        
class Circle:
    def __init__(self, r):
        self._set_radius(r)
        self._area=None
        self._perimeter=None
        
    @property
    def radius(self):
        return self._r
    
    def _set_radius(self, r):
        if isinstance(r, Real) and r>0:
            self.set_radius(r)
            self._area=None
            self._perimeter=None
        else:
            raise ValueError('Radius must be a positive real number!')
    
    @radius.setter
    def radius(self, r):
        self._set_radius(r)
            
    @property
    def area(self):
        if self._area is None:
            self._area=pi*self.radius**2
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter=2*pi*self.radius
        return self._perimeter

class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)
        
    @property
    def radius(self):
        return super().radius
        
        
#test
u=UnitCircle()
print(u.radius, u.area, u.perimeter)




















