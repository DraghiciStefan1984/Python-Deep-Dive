import time


def time_it(fn, *args, rep = 1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    print(str((end - start) / rep))


def compute_powers(n, *, start = 1, end):
    return (n**i for i in range(start, end))


time_it(print, 1, 2, 3, sep = "-", end = "***\n", rep = 5)
time_it(compute_powers, 2, start = 0, end = 20000, rep = 5)