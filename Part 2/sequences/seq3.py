l=[1,2,3,4,5]
print(hex(id(l)))

l[0:3]='python'
print(l)
print(hex(id(l)))