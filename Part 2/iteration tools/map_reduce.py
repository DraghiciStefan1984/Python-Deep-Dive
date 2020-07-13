maps=map(lambda x: x**2, range(10))
print(list(maps))


from itertools import starmap

def add(x, y):
    return x+y

star=list(starmap(add, [(0,0), [1,1], range(2, 4)]))
print(star)


from functools import reduce

red=reduce(lambda x, y: x*y, [1,2,3,4,5,6,7,8])
print(red)


def sum_(iterable):
    it=iter(iterable)
    acc=next(it)
    yield acc
    for item in it:
        acc+=item
        yield acc

for item in sum_([10, 20, 30, 40]):
    print(item)