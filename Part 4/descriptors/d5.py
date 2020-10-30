from numbers import Integral


class IntegerValue:
    def __set__(self, instance, value):
        print('__set__ has been called')
        
    def __get__(self, instance, owner_class):
        print('__get__ has been called')
        
        
class Point:
    x=IntegerValue()
    

p=Point()
p.x=100
print(p.x)


class Person:
    @property
    def age(self):
        return getattr(self, '_age', None)
    
    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('value is not integer')
        if value<0:
            raise ValueError('value is less than zero')
        self._age=value
        
        
p=Person()

try:
    p.age=-9
except ValueError as e:
    print(e)
    
    
class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget=fget
        self.fset=fset
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name=prop_name
        
    def __get__(self, instance, owner_class):
        print('__get__ called')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable')
        return self.fget(instance)
    
    def __set__(self, instance, value):
        print('__set__ called')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable')
        self.fset(instance, value)
        
        
class Person:
    def get_name(self):
        return getattr(self, '_name', None)
    
    def set_name(self, value):
        self._name=value
        
    name=MakeProperty(fget=get_name, fset=set_name)
    
    
p=Person()
p.name='Tom'
print(p.name)