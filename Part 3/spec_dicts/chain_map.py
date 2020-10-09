from collections import ChainMap


d1={'a':1, 'b':2}
d2={'c':3, 'd':4}
d3={'e':5, 'f':6}

d={**d1, **d2, **d3}
print(d)

d={}
d.update(d1)
d.update(d2)
d.update(d3)
print(d)

d=ChainMap(d1, d2, d3)
print(d)

for k, v in d.items():
    print(k, v)
    
    
d1={'a':1, 'b':2}
d2={'c':3, 'd':4}
d3={'a':5, 'b':6}

d=ChainMap(d1, d2, d3)
print(d)

for k, v in d.items():
    print(k, v)
    
d4={'g':7, 'h':8}

print(id(d))

e=ChainMap(d, d4)
print(e)
print(id(e))