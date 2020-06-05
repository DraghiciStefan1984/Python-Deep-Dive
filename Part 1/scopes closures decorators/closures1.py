def outer():
    x='python'
    def inner():
        print(x)
    return inner

f=outer()
print(f.__code__.co_freevars)
print(f.__closure__)


def outer():
    print('\n')
    x=[1,2,3]
    print(hex(id(x)))
    def inner():
        x=[1,2,3]
        print(hex(id(x)))
    return inner

f=outer()
print(f.__code__.co_freevars)
print(f.__closure__)
f()


def outer():
    print('\n')
    x=[1,2,3]
    print(hex(id(x)))
    def inner():
        y=x
        print(hex(id(y)))
    return inner

f=outer()
print(f.__code__.co_freevars)
print(f.__closure__)
f()