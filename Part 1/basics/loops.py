# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:17:18 2020

@author: Stefan Draghici
"""

i=0

while i<10:
    print(i)
    i+=1
    

#break    
i=5

while True:
    print(i)
    if i>=5:
        break
    

#continue
i=0

while i<=10:
    i+=1
    if i%2==0:
        continue
    print(i)


#for   
for i in range(10):
    print(i)
    

for i in range(0, 100, 3):
    print(i)
    
    
for letter in 'hello world':
    print(letter)
    
    
for i,j in [(2,3), ('r','v'), (45, 78)]:
    print(i, j)
    
    
s='sdgavbhada'
i=0

for c in s:
    print(i, c)
    i+=1
    
for i in range(len(s)):
    print(1, s[i])
   
#enumerate will return a tuple with the index of the letter and the letter it's self
for i,c in enumerate(s):
    print(i, c)


#break and continue with exceptions
a=10
b=0

try:
    a/b
except ZeroDivisionError:
    print('division by zero')
finally:
    print('always executes')
    
    
a=0
b=2

while a<4:
    print('-------------------')
    a+=1
    b-=1
    try:
        a/b
    except ZeroDivisionError:
        print('{0}/{1} - division by zero'.format(a, b))
        continue
    finally:
        print('{0}/{1} - always executes'.format(a, b))
    print('{0}/{1} - main loop'.format(a, b))