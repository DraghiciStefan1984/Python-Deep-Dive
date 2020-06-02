def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)


def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1,2,3,4, a=5, b=6, c=7)


def func(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(1,2,3,4,5,6, c=7, d=8, e=9)


def calc_hi_lo_avg(*args, log_to_console=False):
    hi=int(bool(args)) and max(args)
    lo=min(args) if len(args)>0 else 0
    avg=(hi+lo)/2
    if log_to_console:
        print(f'high={hi}, low={lo}, avg={avg}')
    return avg

calc_hi_lo_avg(1,2,3,4,5, log_to_console=True)
print(calc_hi_lo_avg(1,2,3,4,5,6,7,8,9))