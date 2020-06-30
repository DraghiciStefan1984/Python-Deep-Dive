class Squares:
    def __init__(self, length):
        self.length=length
        self.i=0

    def __next__(self):
        if self.i>=self.length:
            raise StopIteration
        else:
            result=self.i**2
            self.i+=1
            return result

    def __iter__(self):
        return self


sq=Squares(3)
print(next(sq))
print(next(sq))
print(next(sq))
# print(next(sq))

sq=Squares(5)

for item in sq:
    print(item)