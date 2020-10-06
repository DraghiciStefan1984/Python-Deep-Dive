s={'a', 100, (20, 33)}
print(s)

s=set()
print(type(s))

s=set([1,2,3])
print(s)

s=set(range(10))
print(s)

s=set({'a': 1, 'b': 2})
print(s)

s={c for c in 'python'}
print(s)

s=set('python')
print(s)

s1={'a', 'b', 'c'}
s2={1, 2, 3}
s={*s1, *s2}
print(s)

print(1 in s)