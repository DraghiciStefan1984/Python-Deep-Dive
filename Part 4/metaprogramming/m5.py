class Metaclass(type):
    def __new__(mcls, name, bases, cls_dict):
        return super().__new__(mcls, name, bases, cls_dict)

class MyClass(metaclass=Metaclass):
    pass

print(type(MyClass))
print(type(MyClass()))


class MyClas(object, metaclass=Metaclass, arg1=10, arg2=20, arg3=30):
    pass