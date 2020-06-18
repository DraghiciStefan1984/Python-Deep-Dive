from collections import namedtuple

Circle=namedtuple('Circle', 'center_x center_y radius')

c=Circle(center_x=12, center_y=55, radius=108)
print(c)