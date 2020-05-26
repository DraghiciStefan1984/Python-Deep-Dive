a=10
b=10

print('a==b', a==b)
print('a is b', a is b)

b=a

print('a==b', a==b)
print('a is b', a is b)

l1=[1,2,3]
l2=[1,2,3]

print('l1==l2', l1==l2)
print('l1 is l2', l1 is l2)


c=int('101', base=2)
print(c)
print(type(c))


def square(x):
    return x**2

def cube(x):
    return x**3

def select_func(func_id):
    if func_id==1:
        return square
    else:
        return cube


print(type(square))
print(select_func(1))
print(select_func(1)(4))
print(select_func(2)(4))


def execute_func(fn, n):
    return fn(n)

print(execute_func(cube, 5))