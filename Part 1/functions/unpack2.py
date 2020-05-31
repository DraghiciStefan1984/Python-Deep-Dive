l1=[1,2,3,4]
l2=[7,8,9,10]
l=[*l1, *l2]
print(l)

s='python'
l=[*l1, *s]
print(l)

s={45, 88, 18}
l=[*l2, *s]
print(l)

d1={'key1':1, 'key2':2}
d2={'key2':3, 'key4':4}
keys={*d1, *d2}
print(keys)

d={**d1, **d2}
print(d)

l=[1,2,3,4,'python']
a, *b, (c, d, *e)=l
print(a, b, c, d, e)