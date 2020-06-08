def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start=perf_counter()
        result=fn(*args, **kwargs)
        end=perf_counter()
        elapsed=end-start
        _args=[str(a) for a in args]
        _kwargs=[f'{k}={v}' for (k, v) in kwargs.items()]
        all_args=_args+_kwargs
        args_str=','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, args_str, elapsed))
        return result
    return inner


# recursive fibo

# @timed
def fibo_rec(n):
    if n<=2:
        return 1
    return fibo_rec(n-1)+fibo_rec(n-2)

@timed
def calc_fibo_rec(n):
    return fibo_rec(n)

fibo_rec(10)
calc_fibo_rec(10)
calc_fibo_rec(35)
calc_fibo_rec(36)


#iter fibo

@timed
def fibo_iter(n):
    fib_1=1
    fib_2=1
    for i in range(3, n+1):
        fib_1, fib_2=fib_2, fib_1+fib_2
    return fib_2

fibo_iter(10)
fibo_iter(35)
fibo_iter(36)


# reduce fibo
from functools import reduce

@timed
def fibo_reduce(n):
    initial=(1, 0)
    dummy=range(n)
    fib_n=reduce(lambda prev, n: (prev[0]+prev[1], prev[0]), dummy, initial)
    return fib_n[0]

fibo_reduce(10)
fibo_reduce(35)
fibo_reduce(36)