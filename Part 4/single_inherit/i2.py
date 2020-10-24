class Shape:
    def __init__(self, name):
        self.name=name
        
    def info(self):
        return f'Shape.info called for Shape({self.name})'
    
    def extended_info(self):
        return f'Shape.extended_info called for Shape({self.name})'
    
    
class Polygon(Shape):
    def __init__(self, name):
        self.name=name
        
    def info(self):
        return f'Polygon.info called for Polygon({self.name})'
    
    
p=Polygon('square')
print(p.info())


class Person:
    def routine(self):
        result=self.eat()
        if hasattr(self, 'study'):
            result+=self.study()
        result+=self.sleep()
        return result
    
    def eat(self):
        return 'Person eats...'
    
    def sleep(self):
        return 'Person sleeps...'


class Student(Person):
    def study(self):
        return 'Student studies...'
        
        
p=Person()
print(p.routine())
s=Student()
print(s.study())
print(s.routine())


class Account:
    apr=3.0
    
    def __init__(self, account_number, balance):
        self.account_number=account_number
        self.balance=balance
        self.account_type='Generic Account'
        
    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR={type(self).apr}'
    
class Savings(Account):
    apr=5.0
    
    def __init__(self, account_number, balance):
        self.account_number=account_number
        self.balance=balance
        self.account_type='Savings Account'
    
a=Account(123, 5000)
print(a.apr)
print(a.calc_interest())

s=Savings(123, 5000)
print(s.apr)
print(s.calc_interest())