l=[1,2,3]
t=(1,2,3)
s='python'

print(l[1], t[1], s[1])
print(l[0:1], t[0:1], s[1:3])


t=([1,2,3], 3.5, 'x')

print(t[0][1])

t[0][1]=88
print(t)

l=[1,2,3,4,5,6,7,8,9]
print(l[:5])
print(l[4:])
print(l[::-1])
print(list(enumerate(s)))

l=[1,2,3]
print(hex(id(l)))

l.clear()
print(hex(id(l)))

l=[1,2,3]
print(hex(id(l)))

l=[]
print(hex(id(l)))


l1=[1,2,3]
l2=[4,5,6]
l1.append(l2)
print(l1)

l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)

l1.extend({'a', 'b', 'c'})
print(l1)