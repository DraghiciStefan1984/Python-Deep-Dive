from collections import namedtuple
import numbers

# Point=namedtuple('Point', 'x y')

class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt=(x, y)
        else:
            raise TypeError('Point coords must be real numbers')

    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, s):
        return self._pt[s]


p1=Point(12, 16)
print(p1)
print(p1[0])

p2=Point(*p1)
print(p2)


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts=[Point(*pt) for pt in pts]
        else:
            self._pts=[]

    def __repr__(self):
        pts_str=', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __setitem__(self, s, value):
        self._pts[s]=[Point(*pt) for pt in value]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts=self._pts+other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with Polygon instance')

    def __iadd__(self, other):
        if isinstance(other, Polygon):
            points=other._pts
        else:
            points=[Point(*pt) for pt in other]
        self._pts=self._pts+points
        return self      

    def append(self, pt):
        self._pts.append(Point(*pt))

    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))

p1=Point(12, 55)
p2=Point(28, 44)
p3=Point(11, 67)
p4=Point(3, 8)
poly=Polygon(p1, p2, p3, p4)
print(poly)
print(poly[0])
print(poly[0:3])
print(poly[::-1])
poly+=[(2, 8), (5, 6)]
print(poly)
poly.append((23, 55))
print(poly)