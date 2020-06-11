def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed=0
        for i in range(reps):
            start=perf_counter()
            result=fn(*args, **kwargs)
            end=perf_counter()
            total_elapsed+=(end-start)
        print('avg run time is {0:.6f}s'.format(total_elapsed/reps))
        return result

    return inner


def calc_fib_rec(n):
    return 1 if n<3 else calc_fib_rec(n-1)+calc_fib_rec(n-2)

def fib(n):
    return calc_fib_rec(n)

fib(30)

fib=timed(fib, 10)

fib(30)


# normal decorator
def dec(fn):
    print('running dec')

    def inner(*args, **kwargs):
        print('runing inner')
        return fn(*args, **kwargs)

    return inner


# decorator factory
def dec_factory():
    print('running dec factory')

    def dec(fn):
        print('running dec')

        def inner(*args, **kwargs):
            print('runing inner')
            return fn(*args, **kwargs)

        return inner

    return dec

@dec_factory()
def func():
    print('func')

func()


#create a decorator factory to be able to use @
# with parameterized decorators

def dec_factory(a, b):
    print('running dec factory')

    def dec(fn):
        print('running dec')

        def inner(*args, **kwargs):
            print('runing inner')
            print(f'a={a}, b={b}')
            return fn(*args, **kwargs)

        return inner

    return dec


@dec_factory(10, 20)
def func():
    print('func')

func()


def dec_facory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed=0
            for i in range(reps):
                start=perf_counter()
                result=fn(*args, **kwargs)
                end=perf_counter()
                total_elapsed+=(end-start)
            print('avg run time is {0:.6f}s, and ran {1} times'.format(total_elapsed/reps, reps))
            return result
        return inner
    return timed


def calc_fib_rec(n):
    return 1 if n<3 else calc_fib_rec(n-1)+calc_fib_rec(n-2)

@dec_facory(10)
def fib(n):
    return calc_fib_rec(n)

fib(30)
