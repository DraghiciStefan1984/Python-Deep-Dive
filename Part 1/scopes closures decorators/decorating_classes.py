from fractions import Fraction
from datetime import datetime


def dec_speak(cls):
    cls.speak=lambda self, message:'{0} says: {1}'.format(self.__class__.__name__, message)
    return cls


Fraction=dec_speak(Fraction)
f=Fraction(2, 3)
print(f.speak('hello'))


@dec_speak
class Person:
    pass

p=Person()
print(p.speak('pers'))

del Person
del p


def info(self):
    results=[]
    results.append(f'time: {datetime.now()}')
    results.append(f'class: {self.__class__.__name__}')
    results.append(f'id: {hex(id(self))}')
    for k, v in vars(self).items():
        results.append('{k}: {v}')
    return results



def debug_info(cls):
    cls.debug=info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name=name
        self.birth_year=birth_year

    def say_hi(self):
        return 'hello'


p=Person('Stefan', 1984)
p.say_hi()
p.debug()