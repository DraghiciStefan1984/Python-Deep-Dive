import sys
import ctypes


x = 10
print(hex(id(x)))

a = [1, 2, 3]
print(sys.getrefcount(a))

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

b = a
print(ref_count(id(a)))
b = None
print(ref_count(id(a)))
a = None
print(ref_count(id(a)))


a = "hello"
print("pointer a is referencing a variable of type: " + str(type(a)))
a = True
print("pointer a is referencing a variable of type: " + str(type(a)))
a = 4
print("pointer a is referencing a variable of type: " + str(type(a)))
a = 3.45
print("pointer a is referencing a variable of type: " + str(type(a)))