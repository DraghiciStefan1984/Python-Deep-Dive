class Person:
    def hello(arg='default'):
        print(f'Hello, with arg={arg}')
        
        
Person.hello()
p=Person()
p.hello()


class MyClass:
    def hello():
        print('hello')
        
    def instance_hello(self):
        print(f'hello from {self}')
        
    @classmethod
    def class_hello(cls):
        print(f'hello from {cls}')
        
    @staticmethod
    def static_hello():
        print('hello from static')
        
        
m=MyClass()
MyClass.hello()
MyClass.class_hello()
# MyClass.instance_hello()
MyClass.static_hello()
# m.hello()
m.class_hello()
m.instance_hello()
m.static_hello()