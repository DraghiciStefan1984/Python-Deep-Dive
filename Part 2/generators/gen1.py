import math


class FactIter:
    def __init__(self, n):
        self.n=n
        self.i=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        else:
            result=math.factorial(self.i)   
            self.i+=1
            return result


fact_iter=FactIter(5)
print(list(fact_iter))
print(list(fact_iter))


def fact():
    i=0
    def inner():
        nonlocal i
        result=math.factorial(i)
        i+=1
        return result
    return inner

f=fact()
print(f())
print(f())
print(f())
print(f())
print(f())


def silly():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

print(next(silly()))
print(next(silly()))
print(next(silly()))
print(next(silly()))
print(next(silly()))

for i in silly():
    print(i)


def fact(n):
    for i in range(n):
        yield math.factorial(i)

gen=fact(8)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))