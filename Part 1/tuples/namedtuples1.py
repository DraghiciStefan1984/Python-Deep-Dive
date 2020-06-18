from collections import namedtuple

Point2D=namedtuple('Point2D', ['x', 'y'])

p1=Point2D(10, 20)
print(p1)

p2=Point2D(78, 105)
print(p1)

Pt2D=namedtuple('Pt2D', ('x', 'y'))


class Point3D:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x==other.x and self.y==other.y and self.z==other.z
        else:
            return False

    def dot_product_3d(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z


# Point3D can be written as a namedtuple
Point3D=namedtuple('Point3D', ('x', 'y', 'z'))

def dot_product_3D(a, b):
    return a.x*b.x+a.y*b.y+a.z*b.z

p1=Point3D(23, 5, 77)
p2=Point3D(88, 19, 78)

# print(list(zip(p1, p2)))
# print([e[0]*e[1] for e in zip(p1, p2)])

def dot_product_3D(a, b):
    return sum([e[0]*e[1] for e in zip(a, b)])

print(dot_product_3D(p1, p2))