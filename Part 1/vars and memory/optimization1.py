############# interning #############

"""Python caches a range of integers in range (-5, 256)
and for larger values it will create new memory addresses.
This no longer applyes."""

a=10
b=10
print(hex(id(a)))
print(hex(id(b)))
print(a==b)
print(a is b)

a=1000
b=1000
print(hex(id(a)))
print(hex(id(b)))
print(a==b)
print(a is b)
