l=[4,5,6,7,8,9,8,7,6]

_max=lambda x, y: x if x>y else y
print(_max(3, 4))

def max_sequence(sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=_max(result, x)
    return result

print(max_sequence(l))

_min=lambda x, y: x if x<y else y

def min_sequence(sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=_min(result, x)
    return result

_add=lambda x, y: x+y

def add_sequence(sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=_add(result, x)
    return result

def _reduce(fn, sequence):
    result=sequence[0]
    for x in sequence[1:]:
        result=fn(result, x)
    return result

print(_reduce(_add, l))
print(_reduce(_min, l))
print(_reduce(_max, l))


# use teh reduce function from functools
from functools import reduce

print('\n********** using reduce from functools ************\n')

l=[1,2,3,4,5,6,7,8]

print(reduce(_max, l))

f=reduce(lambda a, b: a*b, l)
print(f)

# calculate factorial
