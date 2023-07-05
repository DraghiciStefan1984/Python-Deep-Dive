
def fact(n):
    return 1 if n<2 else n * fact(n-1)

fact_list = map(fact, range(8))

for x in fact_list:
    print(x)

l1 = [1,2,3,4,5]
l2 = [11, 22, 33]
rez = list(map(lambda x, y: x+y, l1, l2))
print(rez)

x = range(25)
print(x)
for i in x:
    print(i)

rez = list(filter(lambda x: x % 3 == 0, range(25)))
print(rez)

l1 = [1,2,3,4]
l2 = [12, 56, 89, 90]
l3 = "python"
z = zip(l1, l2, l3)
print(z)
for i in z:
    print(i)

rez = [fact(n) for n in range(20)]
print(rez)

l1 = [1,2,3,4,5,6]
l2 = [10,20,30,40]
print([x+y for x, y in zip(l1, l2)])