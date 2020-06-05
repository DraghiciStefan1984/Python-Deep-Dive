from functools import partial


def func(a, b, c):
    print(a, b, c)

def f(x, y):
    return func(10, x, y)

f(20, 30)

f=partial(func, 10)
f(20, 30)