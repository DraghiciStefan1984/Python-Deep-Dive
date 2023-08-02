t = 1, 2, 5, 'a'
a, b, c, d = t
london = "London", "UK", 9000000
new_york = ("New York", "USA", 8500000)
beijing = "Beijing", "China", 21000000

cities = [london, new_york, beijing]
print([city[2] for city in cities])
print(sum(city[2] for city in cities))


# named tuples
from collections import namedtuple

Point2D = namedtuple("Point2D", ["x", "y"])
p1 = Point2D(10, 20)
p2 = Point2D(40, 22)
print(p1)
print(p2)

Point3D = namedtuple("Point3D", ("x", "y", "z"))

def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 5, 6)
print(dot_product_3d(p1, p2))