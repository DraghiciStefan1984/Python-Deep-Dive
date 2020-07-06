class Squares:
    def __init__(self, n):
        self._n=n
    
    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if i>=self._n:
            raise IndexError
        else:
            return i**2

    
sq=Squares(10)
for i in sq:
    print(i)

sq_iter=iter(sq)
print(type(sq_iter))

print(next(sq_iter))
print(next(sq_iter))
print(next(sq_iter))


class SquaresIterator:
    def __init__(self, squares):
        self._squares=squares
        self._i=0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i>=len(self._squares):
            raise StopIteration
        else:
            result=self._squares[self._i]   
            self._i+=1
            return result


sq=Squares(10)
sq_iter=SquaresIterator(sq)

print(next(sq_iter))
print(next(sq_iter))
print(next(sq_iter))
print(next(sq_iter))


def counter():
    i=0

    def inc():
        nonlocal i
        i+=1
        return i
    return inc