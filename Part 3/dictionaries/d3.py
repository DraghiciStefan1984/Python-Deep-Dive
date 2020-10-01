d1={'a':1, 'b':2, 'c':3}
d2=dict(zip('cde', [30, 18, 88]))

for key in d1:
    print(key)
    
for key in d1.keys():
    print(key)
    
for val in d1.values():
    print(val)
    
for item in d1.items():
    print(item)
    
for k, v in d1.items():
    print(k, v)
    
d1={'a': 1, 'b': 2, 'c': 3}
d2={'b': 30, 'c': 18, 'd':65}
k1=d1.keys()
k2=d2.keys()
print(k1&k2)

new_dict={}
for key in d1.keys()&d2.keys():
    new_dict[key]=d1[key], d2[key]
print(new_dict)

new_dict={key: (d1[key], d2[key]) for key in d1.keys()&d2.keys()}
print(new_dict)

union=d1.keys()|d2.keys()
print(union)

intersection=d1.keys()&d2.keys()
print(intersection)

print(union-intersection)
print(d1.keys()^d2.keys())