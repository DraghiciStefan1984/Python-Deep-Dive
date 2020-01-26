# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:22:45 2020

@author: Stefan Draghici
"""

l=[1,3,2]
t=(7,2,8)
s='python'
st={7,8,9,4,1}

t2=([1,3,2], 'sda', 2)

s2='dfdd sfsddsf sdf sdfsd dsfds'


#test
print(l[1])
print(t[1])
print(s[1])
#print(st[1])

for item in st:
    print(item)
    
print(t2)
t2[0][1]=9
print(t2)

print(min(l))
print(min(t))
print(min(s))
print(min(st))
#print(min(t2))

print(l+[7,8])
print(t+t2)
#print(s+l)
#print(st+s)
print(list(enumerate(s2)))
