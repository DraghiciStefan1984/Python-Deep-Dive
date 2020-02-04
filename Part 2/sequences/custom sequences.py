# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:02:39 2020

@author: Stefan Draghici
"""

import numbers


class Seq:
    def __init__(self, name):
        self.name=name
        
    def __repr__(self):
        return f'Seq(name={self.name})'
    
    def __add__(self, other):
        return Seq(self.name+other.name)
    
    def __iadd__(self, other):
        if isinstance(other, Seq):
            self.name+=other.name
        else:
            self.name+=other
        return self
    
    def __mul__(self, n):
        return Seq(self.name*n)
    
    def __imul__(self, n):
        self.name*=n
        return self
    
    def __contains__(self, value):
        return value in self.name
    
    
class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt=(x, y)
        else:
            raise TypeError
            
    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'
    
    def __len__(self):
        return len(self._pt)
    
    def __getitem__(self, s):
        return self._pt[s]
    
    
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
        try:
            rhs=[Point(*pt) for pt in value]
            is_single=False
        except TypeError:
            try:
                rhs=Point(*value)
                is_single=True
            except TypeError:
                raise TypeError('invalid Point or iterable of points')
        if (isinstance(s, int) and is_single) or (isinstance(s, slice) and not is_single):
            self._pts[s]=rhs
        else:
            raise TypeError('incompatible index/slice assignment')
    
    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts=self._pts+other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with other polygon')
    
    def append(self, pt):
        self._pts.append(Point(*pt))
        
    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))
        
    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts+=pts._pts
        else:
            points=[Point(*pt) for pt in pts]
            self._pts+=points
            
    def __iadd__(self, other):
        self.extend(other)
        return self
    
    def __delitem__(self, s):
        del self._pts[s]
        
    def pop(self, i):
        return self._pts.pop(i)
    
    def clear(self):
        self._pts.clear()
    
    
    
#test
c1=Seq('sdasd')
c2=Seq('uiyi')
print(id(c1), id(c2))
result=c1+c2
print(result)

p=Point(10, 20)
x, y=p
poly1=Polygon((0,0), (4, 8))
print(poly1)
poly2=Polygon((12, 78), (10, 25))
print(poly1+poly2)










