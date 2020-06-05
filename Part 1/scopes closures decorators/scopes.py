a=10

def func(n):
    c=n**2
    return c

def func(n):
    print('global a:', a)
    c=a**n
    return c

print(func(2))


def func(n):
    #this a is local
    a=20
    c=a**n
    return c

print(func(3))
print(a)


def func(n):
    #this a is a reference to the global a
    global a
    a=20
    c=a**n
    return c

print(func(3))
print(a)


def outer_func():
    x='hello'
    def inner_func():
        print(x)
    inner_func()

outer_func()


def outer_func():
    x='hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

outer_func()


def outer_func():
    x='hello'
    def inner():
        x='python'
        print('inner', x)
    inner()
    print('outer', x)

outer_func()


def outer_func():
    x='hello'
    def inner():
        nonlocal x
        x='python'
        print('inner', x)
    inner()
    print('outer', x)

outer_func()