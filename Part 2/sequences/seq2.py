# shallow copy
l1=[1,2,3,4,5]
l1_copy=[]

for item in l1:
    l1_copy.append(item)

print(hex(id(l1)))
print(hex(id(l1_copy)))


l1=[1,2,3,4,5]
l1_copy=[item for item in l1]
print(hex(id(l1)))
print(hex(id(l1_copy)))


l1=[1,2,3,4,5]
l1_copy=list(l1)
print(hex(id(l1)))
print(hex(id(l1_copy)))


v1=[0,0]
v2=[0,0]
line1=[v1, v2]
line2=line1.copy()
print(hex(id(line1[0])), hex(id(line2[0])))
line1[0][0]=100
print(line1)
print(line2)

# deep copy
from copy import deepcopy

v1=[1,1]
v2=[2,2]
v3=[3,3]
v4=[4,4]
line1=[v1, v2]
line2=[v3, v4]
plane1=[line1, line2]
print(plane1)

plane2=deepcopy(plane1)
print(plane1)
print(plane2)
print(hex(id(plane1)), hex(id(plane2)))
print(hex(id(plane1[0])), hex(id(plane2[0])))
print(hex(id(plane1[0][0])), hex(id(plane2[0][0])))