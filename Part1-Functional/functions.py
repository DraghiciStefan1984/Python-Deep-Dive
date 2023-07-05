
def func(a: 'annotation for a', 
         b: 'annotation for b' = 1) -> 'annotation for the retun value':
    return a*b

print(func(3, 5))
print(func(6))


def sq(x):
    return x**2

lsq = lambda x: x**2
print(lsq(5))

g = lambda x, y = 10: x + y
print(g(8))

f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))


def apply_func(fn, *args, **kwargs):
    fn(*args, **kwargs)

print(apply_func(sq, 4))


l1 = [2,3,5,4,6,7]
l2 = ['a', 'U', 's', 'X', 'e']
print(sorted(l2, key=lambda s: s.upper()))

d = {'ghi': 1, 'abc': 5, 'def': 5}
print(sorted(d))
print(sorted(d, key=lambda e: d[e]))