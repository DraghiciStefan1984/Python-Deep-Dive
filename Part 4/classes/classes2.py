class BankAccount:
    apr=1.2


a1=BankAccount()
a2=BankAccount()

print(a1 is a2)
print(a1.__dict__)
print(a1.apr, a2.apr)


BankAccount.account_type='Savings'

print(a1.__dict__)
print(a1.account_type)

a1.apr=0
print(a1.__dict__)
print(a2.__dict__)

a2.apr=23
print(a1.__dict__)
print(a2.__dict__)


class Program:
    langualge='Python'

# create instance attribute
p=Program()
p.__dict__['version']=3.8

print(p.__dict__)
print(p.version)

p2=Program()
p2.version2=4
print(p2.version2)


class Person:
    def say_hello():
        print('hello')

    def say_hello2(*args):
        print('saly hello args: ', args)

    def set_name(instance_obj, new_name):
        instance_obj.name=new_name

Person.say_hello()

p=Person()
p.say_hello

print(type(Person.say_hello))
print(type(p.say_hello))

Person.say_hello2(1,2,3,4,5) 

p=Person()
p.set_name('Mike')
print(p.__dict__)