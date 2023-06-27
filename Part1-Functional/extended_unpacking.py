l = [1, 2, 3, 4, 5]

#a, b = l[0], l[1:]
a, *b = l
print(a, b)

[a, b, c] = "XYZ"
print(a, b, c)

s = {'d', 12, -15, 0}
l = list(s)
print(l)
*c, = s
print(c)

def func(a, b, *args):
    print(a)
    print(b)
    print(args)

func(1, 4, 5, 7, 4, 3, 2, 2)

def avg(*args):
    count = len(args)
    total = sum(args)
    return total / count

print(avg(34, 78))
print(avg(4,5,5,6,7,5,7,6,5,7,5,7))


def func(a, b, *c, d):
    print(a, b, c, d)

func(1, 2, 3, 4, 5, d=6)


def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)


def func(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)

func(1, 2, x=100, y=200, d=20)