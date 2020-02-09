# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:34:06 2020

@author: Stefan Draghici
"""

class Person:
    pass


class Program:
    language='python'
    version='3.6'
    
    def say_hello():
        print(f'Hello from {Program.language}')
        
        
class BankAccount:
    apr=1.2
    

#test
p=Person()
print(type(p))
print(Person.__name__)

prog=Program()
print(prog.version)
prog.version='3.7'
print(prog.version)
print(getattr(Program, 'language'))
setattr(Program, 'test', 'test value')
print(prog.test)
delattr(Program, 'test')
print(list(Program.__dict__.items()))
Program.say_hello()

acc1=BankAccount()
acc2=BankAccount()

#instance attribute
setattr(acc2, 'test', 56)
print(acc2.test)
