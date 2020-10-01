t1=(1,2,3)
t2=(1,2,3)

print(t1==t2)
print(t1 is t2)
print(id(t1), id(t2))
print(hash(t1), hash(t2))

d={t1: 100}
print(d[t1])
print(d[t2])


class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __eq__(self, other):
        return self.name==other.name and self.age==other.age
    
    # overwrite __hash__ so that the object can be hashable
    def __hash__(self):
        return hash((self.name, self.age))
    
    # apply only if we wanth that the object not to be hashable
    #__hash__=None
    
    
p1=Person('Stef', 36)
p2=Person('Stef', 36)

print(p1==p2)
print(p1 is p2)
print(id(p1), id(p2))
print(hash(p1), hash(p2))


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, tuple) and len(other)==2:
            other=Point(*other)
        if isinstance(other, Point):
            return self.x==other.x and self.y==other.y
        
    def __hash__(self):
        return hash((self.x, self.y))
    
    
points={Point(0, 0):'origin', Point(1,1):'second point'}
print(points[Point(0,0)])
print(points[(0,0)])