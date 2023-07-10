

def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function {0} was called {1} times".format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner

def add(a: int, b: int = 0):
    return a + b

def mult(a: int, b: int, c: int = 1):
    return a * b * c


print(hex(id(add)))
add = counter(add)
print(hex(id(add)))
print(add(10, 20))
mult = counter(mult)
print(mult(23, 66))
print(mult(12, 45, c = 80))

@counter
def func(s: str, i: int) -> str:
    return s * i

print(func("hello", 3))


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end  = perf_counter()
        elapsed = end - start
        args_ = [str(a) for a in args]
        kwargs_ = ["{0}={1}".format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ', '.join(all_args)
        print("{0}({1}) took {2:.6f}s to run.".format(fn.__name__, args_str, elapsed))
        return result
    return inner

@timed
def fibo_rec(n):
    if n <= 2:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)
    
fibo_rec(5)

@timed
def fibo_rec_2(n):
    return fibo_rec(n)

fibo_rec_2(5)


@timed
def fibo_loop(n):
    fib1 = 1
    fib2 = 1
    for i in range(3, n + 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2

fibo_loop(5)