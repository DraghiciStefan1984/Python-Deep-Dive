from inspect import getgeneratorstate

def gen(s):
    for c in s:
        yield c


g=gen('abc')

print(getgeneratorstate(g))

print(next(g))
print(getgeneratorstate(g))

print(next(g))
print(getgeneratorstate(g))

print(next(g))
print(getgeneratorstate(g))

# print(next(g))
# print(getgeneratorstate(g))


def echo():
    while True:
        received=yield
        print('you said: ', received)

e=echo()

# print(e.send('hello'))


def squares(n):
    for i in range(n):
        yield i**2

s=squares(5)
print(next(s))
print(next(s))
print(next(s))


def echo(max_times):
    for _ in range(max_times):
        received=yield
        print('You said', received)
    print('that is all')


e=echo(3)
print(next(e))
print(e.send('hello'))