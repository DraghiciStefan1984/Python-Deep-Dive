def fibo_rec(n):
    return 1 if n<=1 else fibo_rec(n-1)+fibo_rec(n-2)

print(fibo_rec(10))
print([fibo_rec(i) for i in range(10)])
# print(fibo_rec(1000))


def fibo_loop(n):
    fib_0=1
    fib_1=1
    for i in range(n-1):
        fib_0, fib_1=fib_1, fib_0+fib_1
    return fib_1

print(fibo_loop(10))
print([fibo_loop(i) for i in range(10)])
print(fibo_loop(1000))


class FibIter:
    def __init__(self, n):
        self.n=n
        self.i=0

    def __iter__(self):
        return self

    def fib(self, n):
        fib_0=1
        fib_1=1
        for i in range(self.n-1):
            fib_0, fib_1=fib_1, fib_0+fib_1
        return fib_1

    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        else:
            result=self.fib(self.i)
            self.i+=1
            return result


fib_iter=FibIter(10)
for num in fib_iter:
    print(num)


# the generator function
def fib_gen(n):
    fib_0=1
    fib_1=1
    for i in range(n-1):
        fib_0, fib_1=fib_1, fib_0+fib_1
        yield fib_1

gen=fib_gen(10)
for num in gen:
    print(num)