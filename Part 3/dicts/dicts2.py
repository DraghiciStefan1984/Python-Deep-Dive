# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:14:28 2020

@author: Stefan Draghici
"""

d=dict(zip('abcfcsdgad', range(1, 100)))
text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas consectetur nisl purus, nec ultrices ligula euismod ac. Phasellus dapibus, risus sollicitudin eleifend lobortis, eros ligula gravida odio, eget mollis dolor tellus sit amet massa. Mauris vulputate arcu massa, a fermentum nibh vulputate et. Nulla porta velit quam, vitae scelerisque diam congue a. Cras massa erat, dapibus nec lacinia imperdiet, tempor non diam. Aenean pellentesque facilisis consequat. Etiam bibendum lacus id enim suscipit iaculis. Integer et dolor sem. Morbi pellentesque leo ac sodales ultricies. Ut ac felis sollicitudin, condimentum massa ac, iaculis dolor. Nulla eu lectus quis lectus suscipit egestas. Maecenas finibus dolor ac magna mollis, eget bibendum quam consequat. Praesent molestie, nunc in venenatis porttitor, ipsum mi volutpat risus, et vulputate nulla leo at justo. Duis a finibus mauris, ut porta dolor. Donec placerat magna lacus, vitae mattis dolor finibus vitae. Etiam non elementum nisl.'

counts=dict()
for c in text:
    counts[c]=counts.get(c, 0)+1
print(counts)


d=dict.fromkeys('dhbhbdaskj', 0)
print(d)
del d['b']
print(d)


#dict views
s1={1,2,3}
s2={2,3,4,5}

print('union: ', s1|s2)
print('intersection: ', s1&s2)
print('diff: ', s1-s2)
print('diff: ', s2-s1)


d1={'a':1, 'b':2, 'c':3}
d2=dict(zip('cde', [48,32,98]))

for key in d1:
    print(key)
    
for key in d1.keys():
    print(key)
    
for item in d1.items():
    print(item)
    
for k, v in d1.items():
    print(k, v)
    
print(d1.items()|d2.items())

d1={'a':1, 'b':2, 'c':3}
d2={'b':15, 'c':21, 'd':33}
d3={}

for key in d1.keys() & d2.keys():
    d3[key]=(d1[key], d2[key])
print(d3)

d3={key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}
print(d3)