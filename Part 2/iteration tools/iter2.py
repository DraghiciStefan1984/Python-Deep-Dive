from itertools import chain, tee

# chaining is used when iterating throu multiple iterables/iterators
# teeing is used hen we need to iteratoe over an iterator multiple times

l1=(i**2 for i in range(4))
l2=(i**2 for i in range(4, 8))
l3=(i**2 for i in range(8, 12))

# for gen in l1, l2, l3:
#     for item in gen:
#         print(item)

l=[l1, l2, l3]

for item in chain(*l):
    print(item)


def squares(n):
    for i in range(n):
        yield i**2

s=squares(10)

print(list(s))

print(s)
iters=tee(s, 5)
print(list(iters))