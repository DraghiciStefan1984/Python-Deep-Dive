s='I work all day and sleep all night!'

iter_s=iter(s)

print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))

class CyclicIterator:
    def __init__(self, lst, length):
        self.lst=lst
        self.length=length
        self.i=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i>=self.length:
            raise StopIteration
        result=self.lst[self.i%len(self.lst)]
        self.i+=1
        return result


cyc_iter=CyclicIterator('abcd', 5)
for item in cyc_iter:
    print(item)