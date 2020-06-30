import random


class RandomNumbers:
    def __init__(self, length, *, min_range=0, max_range=10):
        self.length=length
        self.min_range=min_range
        self.max_range=max_range
        self.num_requested=0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested>=self.length:
            raise StopIteration
        else:
            self.num_requested+=1
            return random.randint(self.min_range, self.max_range)


rn=RandomNumbers(4)
print(next(rn))
print(next(rn))
print(next(rn))
print(next(rn))
print(next(rn))