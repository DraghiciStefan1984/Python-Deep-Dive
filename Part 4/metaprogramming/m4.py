############### class decorator #############

def savings(cls):
    cls.account_type='savings'
    return cls

def cheking(cls):
    cls.account_type='cheking'
    return cls


class Account:
    pass

@savings
class Bank1Savings(Account):
    pass

@cheking
class Bank1Checking(Account):
    pass

print(Bank1Checking.__dict__)


def account_type(type_):
    def decorator(cls):
        cls.account_type=type_
        return cls
    return decorator

@account_type('Savings')
class BankSavings:
    pass

print(BankSavings.__dict__)


def hello(cls):
    cls.hello=lambda self: f'{self} says hello'
    return cls

@hello
class Person:
    def __init__(self, name):
        self.name=name

    def __str__(self):
        return self.name

p=Person('Stefan')
print(p.hello())
print(vars(Person))


from functools import wraps

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result=fn(*args, **kwargs)
        print(f'Log: {fn.__qualname__}({args}, {kwargs})={result}')
        return result
    return inner


def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating...')
            setattr(cls, name, func_logger(obj))
    return cls

@class_logger
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def greet(self):
        return 'Hello, I am {self.name}.'

p=Person('Alex', 65)
p.greet()


############## decorator class ###########
from types import MethodType


class Logger:
    def __init__(self, fn):
        self.fn=fn

    def __call__(self, *args, **kwargs):
        print(f'Log: {self.fn.__name__} called...')
        return self.fn(*args, **kwargs)

    def __get__(self, instance, owner_class):
        print(f'__get__ called: self={self}, instance={instance}')
        if instance is None:
            print('return self unbound')
            return self
        else:
            print('return self as a bound method')
            return MethodType(self, instance)

@Logger
def say_hello():
    pass

say_hello()

class Person:
    def __init__(self, name):
        self.name=NameError

    @Logger
    def say_hello(self):
        return f'{self.name} says hello.'

p=Person('Ana')
p.say_hello()