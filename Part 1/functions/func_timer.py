import time


def time_it(fn, *args, reps=1, **kwargs):
    start=time.perf_counter()
    for i in range(reps):
        fn(*args, **kwargs)
    end=time.perf_counter()
    print((end-start)/reps)

time_it(print, 1,2,3, sep=' - ', end=' *** ')
time_it(print, 1,2,3, reps=10, sep=' - ', end=' *** \n')


def compute_powers_1(n, *, start=1, end):
    results=[]
    for i in range(start, end):
        results.append(n**i)
    return results

print(compute_powers_1(2, end=5))


def compute_powers_2(n, *, start=1, end):
    return [n**i for i in range(start, end)]

print(compute_powers_2(2, end=5))


def compute_powers_3(n, *, start=1, end):
    return (n**i for i in range(start, end))

print(list(compute_powers_3(2, end=5)))


#time the functions
time_it(compute_powers_1, 2, start=0, end=20000, reps=5)
time_it(compute_powers_2, 2, start=0, end=20000, reps=5)
time_it(compute_powers_3, 2, start=0, end=20000, reps=5)