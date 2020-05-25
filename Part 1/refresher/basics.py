############### functions ###############
def func(a, b):
    return a+b

print(func)
print(func(3, 4))
print(func('c', '4'))


def func2():
    return func

print(func2())

f=lambda x: x**3

print(f(9))


############### while ##################
min_length=2

while True:
    name=input('your name: ')
    if len(name)>=min_length and name.isprintable() and name.isalpha():
        break


a=0

while a<100:
    a+=1
    if a%2==0:
        continue
    print(a)
else:
    print('executed if not a break statement')


############## exceptions ###############
a=10
b=0

try:
    a/b
except ZeroDivisionError:
    print('division by zero')
finally:
    print('this will always print')


################# for loop ################
for c in 'hello':
    print(c)

for x in (23, 5, 6, 't', 'g', 'dds'):
    print(x)

for i, j in [(1, 4), (6, 2), (2, 7)]:
    print(i, j)

for i in range(100):
    if i%13==0:
        continue
    print(i)

for index, item in enumerate('asdfghjkjhgfd'):
    print(index, item)