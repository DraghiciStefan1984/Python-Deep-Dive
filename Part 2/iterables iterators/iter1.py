# infinite iterable
class Squares:
    def __init__(self):
        self.i=0

    def next_(self):
        result=self.i**2
        self.i+=1
        return result

sq=Squares()
print(sq.next_())
print(sq.next_())
print(sq.next_())
print(sq.next_())
print(sq.next_())
print(sq.next_())


#finite iterable 1
class Squares:
    def __init__(self, length):
        self.length=length
        self.i=0

    def __len__(self):
        return self.length

    def next_(self):
        if self.i>=self.length:
            raise StopIteration
        result=self.i**2
        self.i+=1
        return result

sq=Squares(3)
print(sq.next_())
print(sq.next_())
print(sq.next_())
# print(sq.next_())


#finite iterable 2
class Squares:
    def __init__(self, length):
        self.length=length
        self.i=0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.i>=self.length:
            raise StopIteration
        result=self.i**2
        self.i+=1
        return result

sq=Squares(3)
print(next(sq))
print(next(sq))
print(next(sq))
# print(next(sq))