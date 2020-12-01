################# __new__  ###############
class Point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

p=object.__new__(Point)
print(type(p))
print(p.__dict__)

p.__init__(10, 18)
print(p.__dict__)


class Point:
    def __new__(cls, x, y):
        print('creating instance...', x, y)
        instance=object.__new__(cls)
        return instance

    def __init__(self, x, y):
        print('init called...', x, y)
        self.x=x
        self.y=y

class Squared(int):
    def __new__(cls, x):
        return super().__new__(cls, x**2)

print(Squared(4))


class Square:
    def __new__(cls, w, l):
        cls.area=lambda self:self.w*self.l
        instance=super().__new__(cls)
        return instance

    def __init__(self, w, l):
        self.w=w
        self.l=l

s=Square(3, 4)
print(s.area())


class Square:
    def __new__(cls, w, l):
        cls.area=lambda self:self.w*self.l
        instance=super().__new__(cls)
        instance.w=w
        instance.l=l
        return instance

s=Square(3, 4)
print(s.area())


############# type  #############
import math

class Circle(object):
    def __init__(self, x, y, r):
        self.x=x
        self.y=y
        self.r=r

    def area(self):
        return math.pi*self.r**2


print('Circle' in globals())
print(type(Circle))


class CustomType(type):
    def __new__(cls, name, bases, class_dict):
        print('custon type creation')
        cls_obj=super().__new__(cls, name, bases, class_dict)
        cls_obj.circle=lambda self:2*math.pi*self.r
        return cls_obj

class_body="""
def __init__(self, x, y, r):
    self.x=x
    self.y=y
    self.r=r

def area(self):
    return math.pi*self.r**2
"""

class_dict={}
exec(class_body, globals(), class_body)

Circle=CustomType('Circle', (), class_dict)

print(type(Circle))