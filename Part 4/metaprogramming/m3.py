import math


class CustomType(type):
    def __new__(cls, name, bases, class_dict):
        cls_obj=super().__new__(cls, name, bases, class_dict)
        cls_obj.circle=lambda self: 2*math.pi*self.r
        return cls_obj


class Circle1(metaclass=type):
    def __init__(self, x, y, r):
        self.x=x
        self.y=y
        self.r=r

    def area(self):
        return math.pi*self.r**2

class Circle2(metaclass=CustomType):
    def __init__(self, x, y, r):
        self.x=x
        self.y=y
        self.r=r

    def area(self):
        return math.pi*self.r**2

print(type(Circle1))
print(type(Circle2))