import sys
import ctypes
import gc

num1=1
num2=1
num3=num1

print(hex(id(num1)))
print(hex(id(num2)))
print(hex(id(num3)))

a=[1,2,3,4,5]
print(hex(id(a)))
print(sys.getrefcount(a)-1)

def get_ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(get_ref_count(id(a)))

b=a
print(get_ref_count(id(a)))

c=a
print(get_ref_count(id(a)))

c=10
print(get_ref_count(id(a)))


def get_object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj)==object_id:
            return 'object exists'


class A:
    def __init__(self):
        self.b=B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a=a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()

a=A()
print(a)
print(hex(id(a)))
print(hex(id(a.b.a)))