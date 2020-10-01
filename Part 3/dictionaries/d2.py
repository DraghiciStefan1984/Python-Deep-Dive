import string


d=dict(zip('abcdef', range(1,6)))
print(d)

print(d.get('a'))
print(d.get('dsad'))
print(d.get('z', 'key does not exist'))

del d['d']
print(d)

result=d.pop('e')
print(result)
print(d)

text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

counts=dict()
for c in text:
    key=c.lower().strip()
    if key:
        counts[c]=counts.get(c, 0)+1
    
print(counts)


d={str(i):i**2 for i in range(10)}
print(d)
print(d.popitem())
print(d.popitem())
print(d.popitem())
print(d)

print(string.ascii_lowercase)
categories={}

for c in text:
    if c!=' ':
        if c in string.ascii_lowercase:
            key='lower'
        elif c in string.ascii_uppercase:
            key='upper'
        else:
            key='other'
        
        if key not in categories:
            categories[key]=set()
        categories[key].add(c)
        
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))
    
def cat_key(c):
    cat_1={' ':None}
    cat_2=dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3=dict.fromkeys(string.ascii_uppercase, 'upper')
    categories=dict(chain(cat_1.items(), cat_2.items, cat_3.items()))
    return categories.get(c, 'other')