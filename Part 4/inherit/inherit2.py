# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:26:54 2020

@author: Stefan Draghici
"""

class Person:
    def routine(self):
        return self.eat()+self.study()+self.sleep()
    
    def eat(self):
        return 'Person eats...'
    
    def sleep(self):
        return 'Person sleeps...'

class Student(Person):
    def study(self):
        return 'Student studies...'
    
#p=Person()
#print(p.routine())

s=Student()
print(s.routine())


class Account:
    apr=3.0
    
    def __init__(self, account_number, balance):
        self.account_number=account_number
        self.balance=balance
        self.account_type='Generic'
        
    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR={self.apr}'
    
class SavingsAccount(Account):
    apr=5.0
    
    def __init__(self, account_number, balance):
        self.account_number=account_number
        self.balance=balance
        self.account_type='Savings'
        
    def calc_interest(self):
        return f'Calc interest on {self.account_type} with APR={self.apr}'