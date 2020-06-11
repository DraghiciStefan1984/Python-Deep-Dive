class DecClass:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def __call__(self, c):
        print(f'called a={self.a}, b={self.b}, c={c}')


decClass=DecClass(10, 20)
decClass(100)



class DecClass2:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: a={self.a}, b={self.b}')
            return fn(*args, **kwargs)
        return inner


@DecClass2(10, 20)
def func():
    print('dec func')

func()