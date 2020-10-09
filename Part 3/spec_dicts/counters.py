from collections import defaultdict, Counter


sentence='gvdkqbhja dasjhdasjbnajhsd shdvahsdbash xhas xhaxjhasbxa'

counter=defaultdict(int)
for c in sentence:
    counter[c]+=1
print(counter)


counter=Counter()
for c in sentence:
    counter[c]+=1
print(counter)


c1=Counter('able was I ere I saw elba')
print(c1)

c2=Counter([1,2,3,4,5,6,7,8,9])
print(c2)


import random

random.seed(0)
rand_ints=[random.randint(0, 100) for _ in range(1000)]
c=Counter(rand_ints)
print(c)

c1=Counter(a=2, b=10)
c2=Counter(a=10, b=6)
print(c1+c2)
print(c1-c2)