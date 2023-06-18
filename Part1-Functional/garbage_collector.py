import ctypes
import gc


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "öbject exists"
    return "object not found"

class A:
    def __init__(self):
        self.b = B(self)
        print("A: self: {0}, b: {1}".format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print("B: self: {0}, a: {1}".format(hex(id(self)), hex(id(self.a))))


gc.disable()
a = A()
print(hex(id(a.b)))
print(hex(id(a.b.a)))