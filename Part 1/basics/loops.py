# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:43:11 2019

@author: Stefan Draghici
"""

i=0
while i<5:
    print(i)
    i+=1
    
#emulate a do while loop
i=5
while True:
    print('Test')
    if i>=5:
        break
        print('This will never execute')
        
#continue
a=0
while a<10:
    a+=1
    if a%2==0:
        continue
    print(a)
    
#break
l=[1,2,3]
val=10
found=False
index=0

while index<len(l):
    if l[index]==val:
        found=True
        break
    index+=1
if not found:
    l.append(val)
    
#try finally else
a=10
b=1
try:
    a/b
except ZeroDivisionError:
    print('errrrror')
finally:
    print('always executes')
    
a=0
b=2
while a<4:
    print('--------------')
    a+=1
    b-=1
    try:
        a/b
    except ZeroDivisionError:
        print('div by 0')
        continue
    finally:
        print('always runs')
else:
    print('executed without error')