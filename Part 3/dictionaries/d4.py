d1={'a':1, 'b':2}
d2={'c':3, 'd': 4}
d1.update(d2)
print(d1)

d={**d1, **d2}
print(d)

conf_defaults=dict.fromkeys(('host', 'port', 'user', 'pass', 'db'), None)

print(conf_defaults)

conf_global={'port':2344, 'db':'database'}
conf_dev={'host': 'localhost', 'user': 'test', 'pass':'testpass'}
conf_prod={'host': 'prod.host', 'user': '$test', 'pass':'$pass', 'db':'prod_db'}
conf={**conf_defaults, **conf_global, **conf_dev}
print(conf)


################# shallow copy #############
print('shallow copy\n')
d1={'a': [1, 2], 'b': [3, 4]}
d2=d1.copy()
print(d1 is d2)
print(d1==d2)
print(id(d1), id(d2))
print(d1['a']==d2['a']) 
d1['a'].append(100)
print(d1['a']==d2['a'])


################# deep copy #############
from copy import deepcopy

print('\ndeep copy\n')
d1={'a': [1, 2], 'b': [3, 4]}
d2=deepcopy(d1)
print(d1 is d2)
print(d1==d2)
print(id(d1), id(d2))
print(d1['a']==d2['a']) 
d1['a'].append(100)
print(d1['a']==d2['a']) 

d1=dict(d1)
print(d1 is d2)
print(d1==d2)
print(id(d1), id(d2))