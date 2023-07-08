def outer():
    x = 'python'

    def inner():
        print(x)

    return inner

fn = outer()
fn()


def outer():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count
    
    return inc

fn = outer()
print(fn.__code__.co_freevars)


class Averager:
    def __init__(self) -> None:
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        return sum(self.numbers) / len(self.numbers)

print('***********************')
a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))
print(a.add(40))


def averager():
    numbers  = []

    def add(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)

    return add

print('***********************')
a = averager()
print(a(10))
print(a(20))
print(a(30))
print(a(40))


def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total / count
    
    return add

print('***********************')
a = averager()
print(a(10))
print(a(20))
print(a(30))
print(a(40))


from time import perf_counter

class Timer:
    def __init__(self) -> None:
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()
print(t1())


def timer():
    start = perf_counter()

    def poll():
        return perf_counter() - start
    
    return poll