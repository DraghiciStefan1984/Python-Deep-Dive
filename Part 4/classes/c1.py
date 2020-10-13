class Person:
    pass

print(type(Person))
print(Person.__name__)

p=Person()
print(type(p))
print(p.__class__)
print(isinstance(p, Person))


class Program:
    language='Python'
    version='3.6'
    
    def say_hello():
        print(f'Hello from {Program.language}')
    
print(Program.version)
Program.version='3.8'
print(Program.version)
print(getattr(Program, 'x', 'N/A'))
print(Program.__dict__)
print(Program.__dict__['language'])
print(Program.__dict__['say_hello'])
getattr(Program, 'say_hello')

p=Program()

print(p.__dict__)
print(Program.__dict__)


class Account:
    apr=1.2
    
print(Account.__dict__)

a=Account()
print(a.__dict__)
print(a.apr)

Account.account_type='Savings'
print(Account.__dict__)