t=(1,2,3)
print(type(t))

t=(1,)
print(type(t))

a, b, c=[1, 4, 67]
print(a, b, c)

(a, b)=(1, 3)
print(a, b)

a, b=10, 20
print(a, b)

d={'a':1, 'b':2, 'c':3, 'd':4}
a, b, c, d=d
print(a, b, c, d)

d={'a':1, 'b':2, 'c':3, 'd':4}
a, b, c, d=d.values()
print(a, b, c, d)

d={'a':1, 'b':2, 'c':3, 'd':4}
a, b, c, d=d.items()
print(a, b, c, d)

