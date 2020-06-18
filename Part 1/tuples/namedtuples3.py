from collections import namedtuple

from random import randint, random
from collections import namedtuple

Color=namedtuple('Color', 'red green blue alpha')

def random_color():
    red=randint(0, 255)
    green=randint(0, 255)
    blue=randint(0, 255)
    alpha=round(random(), 2)
    # return red, green, blue, alpha
    return Color(red, green, blue, alpha)


data_dict=dict(key1=100, key2=200, key3=300)

Data=namedtuple('Data', data_dict.keys())
d1=Data(2, 3, 4)
print(d1)

d2=Data(*data_dict.values())
print(d2)

d3=Data(**data_dict)
print(d3)