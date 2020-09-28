d={'a':100, 'b':200}
print(type(d))
print(d['a'])
print(d.get('a'))

print(hash((1,2,3,4)))
print(hash((1,2,3,4)))
print(hash((1,2,3,4)))

d={(1,2,3):'this is a tuple'}
print(d[(1,2,3)])


def fn_add(a, b):
    return a+b

def fn_invert(a):
    return 1/a

def fn_multiply(a, b):
    return a*b

funcs={fn_add: (10, 30), fn_invert: (88, ), fn_multiply: (-12, 67)}

for f in funcs:
    print(f)
    
for f in funcs:
    result=f(*funcs.get(f))
    print(result)

for f, args in funcs.items():
    print(f(*args)) 
        
#############################

d=dict(a=100, b=800)
print(d)

d=dict([('a', 600), ('b', 300), ('c', 900)])
print(d)

###############################
keys=['a','b','c']
values=[1,2,3]

d={}
for k, v in zip(keys, values):
    d[k]=v
    
print(d)

d={k:v for k, v in zip(keys, values)}
print(d)

##############################

x_coords=(-2, -1, 0, 1, 2)
y_coords=(-2, -1, 0, 1, 2)

grid=[(x, y) for x in x_coords for y in y_coords]
print(grid)

import math

grid_extended=[(x, y, math.hypot(x, y)) for x, y in grid]
print(grid_extended)

grid_extended={(x, y): math.hypot(x, y) for x, y in grid}
print(grid_extended)