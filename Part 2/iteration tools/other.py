l1=[1,2,3,4,5]
l2=[1,2,3,4]
l3=[1,2,3]

rez=zip(l1, l2, l3)
print(list(rez))


from itertools import zip_longest

print(list(zip_longest(l1, l2, l3, fillvalue='N/A')))
