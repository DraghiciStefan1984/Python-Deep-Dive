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

l=[1,2,3,4,5,6]
a=l[0]
b=l[1:]
print(a, b)

a, b=l[0], l[1:]
print(a, b)

a, *b=l
print(a, b)

s='python'
a, *b=s
print(a, b)

t=('a', 'b', 'c')
a, *b=t
print(a, b)

[a, b, c]='xyz'
print(a, b, c)

a, b, *c='python'
a, b, *c, d='python'
print(a, b, c, d)

a, b, c, d=s[0], s[1], s[2:-1], s[-1]
print(a, b, c, d)