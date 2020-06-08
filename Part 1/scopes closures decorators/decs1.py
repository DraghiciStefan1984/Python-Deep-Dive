def count(fn):
    count=0

    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print('function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    inner.__name__=fn.__name__
    inner.__doc__=fn.__doc__
    return inner


def add(a:int=0, b:int=0):
    """adds two integers"""
    return a+b

print(hex(id(add)))

# help(add)

add=count(add)
print(hex(id(add)))
print(add(2, 4))


def mult(a, b, c, *, d):
    """multiplies values"""
    return a*b*c*d


mult=count(mult)
print(mult(10, 23, c=0, d=34))


#using wraps to prevent name and doc override
from functools import wraps

def count(fn):
    count=0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        print('function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner