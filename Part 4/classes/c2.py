from types import MethodType


class Person:
    def say_hello(*args):
        print('hello', args)
        
        
Person.say_hello()
p=Person()
p.say_hello()


class Person:
    def say_hello(self):
        print(f'{self} says hello')
        
Person.say_hello(hex(id(Person.say_hello)))
p=Person()
p.say_hello()

p.some_func=lambda *args: print(f'some_func called with {args}')
p.some_func()


class Person:
    def __init__(self, name):
        self.name=name
        
    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))
        
    def do_work(self):
        do_work_method=getattr(self, '_do_work', None)
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('you must register a do work method.')
        
        
math_teacher=Person('Eric')
english_teacher=Person('John')

def work_math(self):
    print('derrivatives')
    
math_teacher.register_do_work(work_math)
math_teacher.do_work()