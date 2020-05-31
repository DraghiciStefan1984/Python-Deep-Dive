def func(a, b, *c):
    print(a)
    print(b)
    print(c)

func(2, 3)
func(5,6,7,8,9,8,7,6)


def avg(*args):
    print(args)
    count=len(args)
    total=sum(args)
    # return total/count if count>0 else 0
    return count and total/count

print(avg(23, 55))
print(avg(34,56,78,95,6))
print(avg())


def func1(a, b, *args, c):
    print(a, b, args, c)

func1(1,2,3,4,5,6,c=7)

#by using *,  no positional arguments will be allowed
# def func2(*, x):
#     print(x)

# func2(1,2,3,4,5)

# a function with two positional arguments,
# then no more postional arguments, then a kwyword argument
def func(a, b, *, c):
    print(a, b, c)

func(2,3,c=7)


def func(a=0, b=0):
    return a+b

print(func())
print(func(10))
print(func(10, 34))