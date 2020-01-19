# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:04:29 2020

@author: Stefan Draghici
"""

from fractions import Fraction
from datetime import datetime, timezone

#add custom funcionality to the class
Fraction.is_integral=lambda self: self.denominator==1

def decorate_speak(cls):
    cls.speak=lambda self, message: '{0} says {1}'.format(self.__class__.__name__, message)
    return cls

Fraction=decorate_speak(Fraction)


def info(self):
    results=[]
    results.append('time: {}'.format(datetime.now(timezone.utc)))
    results.append('class: {}'.format(self.__class__.__name__))
    results.append('id: {}'.format(hex(id(self))))
    for k, v in vars(self).items():
        results.append('{0}:{1}'.format(k, v))
    return results

def debug_info(cls):
    cls.debug=info
    return cls
    
@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name=name
        self.birth_year=birth_year
        
    def say_hi(self):
        return 'hello'
    
    
@debug_info
class Auto:
    def __init__(self, make, model, year, top_speed):
        self.make=make
        self.model=model
        self.year=year
        self.top_speed=top_speed
        self.speed=0
        
    @property
    def speed(self):
        return self.speed
    
    @speed.setter
    def speed(self, value):
        if value>self.top_speed:
            self.speed=self.top_speed
        else:
            self.speed=value

#test
f=Fraction(2,3)
print(f.speak('sda'))

p=Person('James', 1900)
p.debug()

a=Auto('mercedes', 's500', 2020, 180)
print(a.debug())

