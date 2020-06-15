t=(1, 2, 3, 'abc', 'a', True, [], None)

a, *b = t
print(a, b)

a, *_, c = t
print(a, c)

t[-2].append([1,2,3])
print(t)

print(list(t))