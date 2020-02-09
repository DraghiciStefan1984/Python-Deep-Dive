# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:09:33 2020

@author: Stefan Draghici
"""

class Person:
    pass

#test
p1=Person()
p2=Person()
p1.name='Stefan'
print(p1.__dict__)
print(p2.__dict__)



class Person:
    def __init__(self, name):
        self.set_name(name)
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._name=value
        else:
            raise ValueError('name can only be a non empty string')
            
    def del_name(self):
        print('deleter called')
        del self.name
            
    name=property(fget=get_name, fset=set_name, fdel=del_name)
            
#test
p1=Person('test')
#p1.set_name(4864)
p1.set_name('Stef')
p2=Person('Ana')
p2.name='Vali'
print(p2.name)



class Person:
    def __init__(self, name):
        self._name=name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._name=value
        else:
            raise ValueError('name can only be a non empty string')
            
    @name.deleter
    def name(self):
        del self._name
            
p1=Person('test')
#p1.name(4864)
p1.name='Stef'
print(p1.name)
p2=Person('Ana')
p2.name='Vali'
print(p2.name)
