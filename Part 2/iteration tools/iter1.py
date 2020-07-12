import math 


l=[2,1,3,0,4,6,5]

print(min(l))
print(max(l))
print(any(l))
print(all(l))


def factorials(n):
    for i in range(n):
        yield math.factorial(i)


def slice_(iterable, start, stop):
    for _ in range(0, start):
        next(iterable)
    for _ in range(start, stop):
        yield next(iterable)


print(list(slice_(factorials(100), 0, 10)))


def factorials2(n):
    index=0
    while True:
        yield math.factorial(index)
        index+=1


def gen_cubes(n):
    for i in range(n):
        yield i**3

def is_odd(x):
    return x%2==1

filtered=filter(is_odd, gen_cubes(10))
print(list(filtered))


from itertools import dropwhile, takewhile
from math import sin, pi

def sin_wave(n):
    start=0
    max_=2*pi
    step=(max_-start)/(n-1)

    for _ in range(n):
        yield round(sin(start), 2)
        start+=step

print(list(sin_wave(15)))

result=takewhile(lambda x: 0<=x<=0.9, sin_wave(90))
print(list(result))