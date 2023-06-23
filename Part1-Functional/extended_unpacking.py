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