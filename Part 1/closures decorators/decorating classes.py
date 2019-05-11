#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:19:15 2019

@author: stefan
"""

from fractions import Fraction

Fraction.speak=lambda self, message:'Fraction says {0}'.format(message)
f=Fraction()
print(f.speak('test'))

Fraction.is_integral=lambda self: self.denominator==1
f1=Fraction(2, 3)
f2=Fraction(64, 8)
print(f1.is_integral())
print(f2.is_integral())

def decorate_speak(cls):
    cls.speak=lambda self, message: '{0} says {1}'.format(self.__class__.__name__, message)
    return cls

Fraction=decorate_speak(Fraction)

f1=Fraction()
print(f1.speak('hello'))

class Person:
    pass

Person=decorate_speak(Person)
p=Person
print(p.speak('this also works'))