# a frozen set is an immutable set but can contain mutable elements (hashable)
s1=frozenset(({'a', 'b'}))
s2=frozenset(({'c', 'd'}))
print(type(s1))
print(type(s2))

s={s1, s2}
print(s)
print(type(s))

################# dict views #############
d={'a': 1, 'b': 2}
keys=d.keys()
values=d.values()
items=d.items()
print(keys)
print(values)
print(items)
print(id(keys))
print(id(values))
print(id(items))

d=dict(zip('abc', range(1, 4)))
for k, v in d.items():
    print(k, v)
    d['c']=1000