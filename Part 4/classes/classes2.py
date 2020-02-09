# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:41:23 2020

@author: Stefan Draghici
"""

class Person:
    def hello(*args):
        print('hello: ', args)
        
#test
Person.hello()
p=Person()
p.hello()



class Person:
    def set_name(inst, name):
        inst.name=name
        
#test
p1=Person()
p2=Person()
Person.set_name(p2, 'John')
print(p2.name)



class Person:
    def hello(self):
        print(f'{self} says hello.')
        
#test
print(Person.hello)
p=Person()
print(p.hello)