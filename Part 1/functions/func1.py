def func1(a, b, c):
    print(f'a={a}, b={b}, c={c}')

func1(3, 45, 66)


def func2(a, b=4, c=1):
    print(f'a={a}, b={b}, c={c}')

func2(8)
func2(11, 3)
func2(11, c=22)
func2(c=22, a=44, b=88)