#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:19:15 2019

@author: stefan
"""

from datetime import datetime, timezone
from math import sqrt


def info(self):
    results=[]
    results.append('Class: {}'.format(self.__class__.__name__))
    results.append('time: {}'.format(datetime.now(timezone.utc)))
    results.append('id: {}'.format(hex(id(self))))
    
    for k, v in vars(self).items():
        results.append('{0}: {1}'.format(k, v))
    return results
    
def debug_info(cls):
    cls.debug=info
    return cls


@debug_info
class Person:
    def __init__(self, name, year):
        self.name=name
        self.year=year
        
    def say_hi():
        return 'Hello, stranger!'
    

p=Person('Stefan', 1984)
print(p.debug())


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make=make
        self.model=model
        self.year=year
        self.top_speed=top_speed
        self._speed=0
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):
        if new_speed>self.top_speed:
            raise ValueError('Speed cannot exceed Top Speed')
        else:
            self._speed=new_speed


a=Automobile('ford', 'model T', 1908, 80)
print(a.debug())


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __abs__(self):
        return sqrt(self.x**2+self.y**2)
        
    def __repr__(self):
        return 'Return({0}, {1})'.format(self.x, self.y)


p1, p2, p3=Point(2,3), Point(4, 5), Point(0, 0)



