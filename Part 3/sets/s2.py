from timeit import timeit


n=100000
s={i for i in range(n)}
l=[i for i in range(n)]
t=(i for i in range(n))
d={i:None for i in range(n)}

repeats=1000000
num=8

repeats=1000
num=99999

# t_list=timeit(f'{num} in l', globals=globals(), number=repeats)
# t_tuple=timeit(f'{num} in t', globals=globals(), number=repeats)
# t_dict=timeit(f'{num} in d', globals=globals(), number=repeats)
# t_set=timeit(f'{num} in s', globals=globals(), number=repeats)

# print(t_list)
# print(t_tuple)
# print(t_dict)
# print(t_set)


s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
print(s1.intersection(s2))
print(s1.intersection(s2, s3))
print(s1 & s2 & s3)
print(s1.union(s2))
print(s1 | s2)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))

