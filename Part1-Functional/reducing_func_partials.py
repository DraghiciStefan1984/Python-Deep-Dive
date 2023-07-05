
l = [2, 5, 1, 7, 3, 10]

_max = lambda x, y: x if x > y else y

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))

_add = lambda x, y: x + y

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print(_reduce(_max, l))
print(_reduce(_add, l))


# partial functions

def func(a, b, c):
    print(a, b, c)

func(10, 20, 30)

def f(x, y):
    return func(10, x, y)

f(20, 30)

from functools import partial

f = partial()