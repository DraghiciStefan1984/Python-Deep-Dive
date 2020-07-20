class Person:
    def __init__(self):
        print(f'initializing a person: {self}.')


class Person:
    pass


p1=Person()
p2=Person()

p1.name='Alex'
print(p1.__dict__)

p2.age=23
print(p2.__dict__)

p1.say_hello=lambda: 'hello!'
print(p1.say_hello())


#add a function to an instance as a method
from types import MethodType

class Person:
    def __init__(self, name):
        self.name=name

p1=Person('Eric')
p2=Person('Alex')

def say_hello(self):
    return f'{self.name} say hello!'

p1_say_hello=MethodType(say_hello, p1)
print(type(p1_say_hello))

p1.hello=p1_say_hello
print(p1.__dict__)
print(p1.hello())