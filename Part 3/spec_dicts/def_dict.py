from collections import defaultdict


d={}
# print(d['a'])
result=d.get('a')
print(result)

sentence='I love coding, makes me happy'
counts=defaultdict(lambda: 0)

for c in sentence:
    counts[c]+=1
    
print(type(counts))
print(isinstance(counts, dict))
print(counts['z'])