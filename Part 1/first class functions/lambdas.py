def sq(x):
    return x**2

l=lambda x: x**2

print(l)
print(l(4))

f=lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'a', 'b', y=10, a=23, b=34, c=55))


def apply_func(x, fn):
    return fn(x)

print(apply_func(4, sq))
print(apply_func(30, lambda x: x**3))