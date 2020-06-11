def fib(n):
    return 1 if n<=2 else fib(n-1)+fib(n-2)


# using class
class Fib:
    def __init__(self):
        self.cache={1:1, 2:1}

    def fib(self, n):
        if n not in self.cache:
            print('calculating fib({})'.format(n))
            self.cache[n]=self.fib(n-1)+self.fib(n-2)
        return self.cache[n]


f=Fib()
f.fib(20)


# using closure
def fib():
    cache={1:1, 2:1}

    def calc_fib(n):
        if n not in cache:
            cache[n]=calc_fib(n-1)+calc_fib(n-2)
        return cache[n]
    
    return calc_fib


#using decorator
def memoize_fib(fib):
    cache={1:1, 2:1}

    def inner(n):
        if n not in cache:
            print('calculating fib({})'.format(n))
            cache[n]=fib(n)
        return cache[n]

    return inner


def memoize_fib(fn):
    cache=dict()

    def inner(n):
        if n not in cache:
            cache[n]=fn(n)
        return cache[n]

    return inner
        