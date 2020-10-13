from math import pi


class Circle:
    def __init__(self, radius):
        self._radius=radius
        self._area=None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._area=None
        self._radius=value
    
    @property    
    def area(self):
        if self._area is None:
            print('calculating area...')
            self._area=pi*(self.radius**2)
        return self._area
    
    
c=Circle(20)
print(c.area)
print(c.area)
print(c.area)


class Person:
    def __init__(self, name):
        self._name=name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name=value
            
    @name.deleter
    def name(self):
        del self._name
        

p=Person('Mike')
print(p.__dict__)
del p.name
print(p.__dict__)