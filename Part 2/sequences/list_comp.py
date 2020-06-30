squares=[x**2 for x in range(100)]
print(squares)

evens=[i for i in range(100) if i%2==0]
print(evens)

table=[[i*j for i in range(11)] for j in range(11)]
print(table)

#calculate pascal triangle
from math import factorial

def combo(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

size=10

pascal=[[combo(n, k) for k in range(n+1)] for n in range(size+1)]
print(pascal)

l1=['a','b','c']
l2=['x','y','z']

result=[s1+s2 for s1 in l1 for s2 in l2]
print(result)

l1=[1,2,3,4,5,6,7,8,9]
l2=['a','b','c','d','e']

result=[(item1, item2) for index1, item1 in enumerate(l1) for index2, item2 in enumerate(l2) if index1==index2]
print(result)

funcs=[lambda x: x**i for i in range(10)]
print(funcs[0](10))
print(funcs[2](3))