class Shape:
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Polygon(Shape):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Triangle(Polygon):
    pass


print(issubclass(Ellipse, Shape))
print(issubclass(Circle, Shape))
print(issubclass(Circle, Ellipse))

s=Shape()
c=Circle()
sq=Square()
p=Polygon()

print(isinstance(s, Shape))
print(isinstance(c, Circle))
print(isinstance(c, Shape))
print(isinstance(sq, Square))

print(type(s))
print(type(c))
print(type(sq))

print(isinstance(sq, type(sq)))
print(isinstance(sq, type(p)))

print(issubclass(Shape, object))


# the object class
print(type(object))

class Person:
    pass

print(issubclass(Person, object))

import math
print(type(math))
print(issubclass(math, object))


def func():
    pass

print(type(func))
