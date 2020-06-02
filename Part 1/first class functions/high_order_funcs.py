def factorial(n):
    return 1 if n<2 else n*factorial(n-1)


# map() applies a function to the elements of an iterable
# and it will return a generator, unless we put the result into a list
factorials=map(factorial, range(10))
# print(list(factorials))

print('first iteration')
for x in factorials:
    print(x)

# the second iteration will return nothing
# as the first iteration exhausted all the elements
print('second iteration')
for x in factorials:
    print(x)

factorials=map(factorial, range(10))
factorials_list=list(factorials)

print('first iteration')
for x in factorials:
    print(x)

print('second iteration')
for x in factorials:
    print(x)

l1=[1,2,3,4]
l2=[10,20,30]
l3=100,200,300,400

sum_of_lists=list(map(lambda x, y: x+y, l1, l2))
print(sum_of_lists)

sum_of_lists=list(map(lambda x, y, z: x+y+z, l1, l2, l3))
print(sum_of_lists)


# filter() will return a filter object
# that will contain the elements from an iterable
# that comply to a certain condition
mod_three=list(filter(lambda x: x%3==0, range(100)))
print(mod_three)

print(list(filter(None, [1, 3, 0, -1, 'a', 'c', False, True, None])))


# zip() combines the elements from two or more iterables to
# a list of tuples with the length of the smallest iterable
l1=[1,2,3,4,5,6,7]
l2=('a','b','c','d','e','f','g','h','i','j','k')
l3='python'
print(list(zip(l1, l2, l3)))


# list comps
l1=[1,2,3,4,5,6,7]
l2=[45,67,65,43,56,78,98,76]
l=[x+y for x, y in zip(l1, l2)]
print(l)

l=[x+y for x, y in zip(l1, l2) if (x+y)%2==0]
print(l)