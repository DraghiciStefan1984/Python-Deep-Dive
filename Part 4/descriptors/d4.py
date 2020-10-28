import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address)


class Person:
    def __init__(self, name):
        self.name=name
        
    def __repr__(self):
        return f'Person(name={self.name})'
    
    
p1=Person('Vali')
p2=p1
print(ref_count(id(p1)))
del p1
# print(ref_count(id(p1)))


import weakref

class IntegerValue:
    def __init__(self):
        self.values=weakref.WeakKeyDictionary()
        
    def __set__(self, instance, value):
        self.values[instance]=int(value)
    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)
        
class Point:
    x=IntegerValue()
        
p=Point()
p.x=100.1
print(Point.x.values.keyrefs)


class IntegerValue:
    def __init__(self):
        self.values={}
        
    def __set__(self, instance, value):
        self.values[id(instance)]=int(value)
    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))
        
class Point:
    x=IntegerValue()

    def __init__(self, x):
        self.x=x
        
    def __eq__(self, other):
        return isinstance(other, Point) and self.x==other.x
    
    