

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("{0}: called {1}".format(run_dt, fn.__name__))
        return result
    
    return inner


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
@logged
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))

print(fact(10))


# param decorators

def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0

        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end  = perf_counter()
            total_elapsed += (end - start)

        avg_runtime = total_elapsed / reps
        print("Avg run time: {0:.6f}".format(avg_runtime))
        return result

    return inner


def fibo_rec(n):
    return 1 if n < 3 else fibo_rec(n - 2) + fibo_rec(n - 1)


def decorator_factory():
    print("running dec factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            return fn(*args, **kwargs)
        
        return inner

    return dec

@decorator_factory()
def func():
    print("running func")


# dec class

def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("decorated funcion called: a={0}, b={1}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print("hello {0}".format(s))

my_func("Fane")

class MyClass:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def __call__(self, c):
        print("called a={0}, b={1}, c={2}".format(self.a, self.b, c))

obj = MyClass(10, 20)