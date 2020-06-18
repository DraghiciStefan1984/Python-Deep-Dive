from collections import namedtuple

Circle=namedtuple('Circle', 'center_x center_y radius')

c=Circle(center_x=12, center_y=55, radius=108)
print(c)
print(c._asdict())


Point2D=namedtuple('Point2D', 'x y')
p=Point2D(23, 44)
print(p)


Stock=namedtuple('Stock', 'symbol year month day open high low close')
djia=Stock('DJIA', 2019, 1, 23, 23444, 23823, 23002, 23500)
print(djia)

print(hex(id(djia)))

#replace a value using _replace
djia=djia._replace(year=2020)
print(hex(id(djia)))
print(djia)

#add a new field
# Point3D=Point2D._fields+('z',)
Point3D=namedtuple('Point3D', Point2D._fields+('z',))
p3D=Point3D(23, 55, 66)
print(p3D)


Vector2D=namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
v1=Vector2D(0, 0, 10, 10, 0, 0)

# one way to add default values by creating a prototype instance
# of the naped tuple with the default values
vector_zero=Vector2D(0,0,0,0,0,0)

v2=vector_zero._replace(x1=20, y1=67, x2=34, y2=77)
print(v2)


# another way is to modify __defaults__ which will add defaults
# starting from the last argument fo the first
Vector2D.__new__.__defaults__=(0,0)
v1=Vector2D(10,10)
print(v1)