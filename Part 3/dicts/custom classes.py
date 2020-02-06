# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:24:27 2020

@author: Stefan Draghici
"""

t1=(1,2,3)
t2=(1,2,3)

print(id(t1), id(t2))
print(hash(t1), hash(t2))


class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name==other.name and self.age==other.age
        else:
            return False
        
    #if we don't want the class to be hashable
    #__hash__=None
        
    def __hash__(self):
        return hash(self.name, self.age)
    
#test
p1=Person('John', 28)
p2=Person('John', 28)
print(p1 is p2)
print(p1==p2)

p1=Person('John', 28)
p2=Person('Eric', 35)
persons={p1:'John object', p2:'Eric object'}
print(persons[p1])