class Person:
    pass

p=Person()
print(type(p))
print(Person.__name__)
print(type(Person))


class Program:
    language='Python'
    version=3.6

print(Program.language)
print(Program.version)

setattr(Program, 'version', 2.6)
print(Program.version)

Program.version=3.9
print(Program.version)

setattr(Program, 'x', 100)
print(Program.x)

p=Program()
print(p.x)

print(Program.__dict__)
# Program.__dict__['new_attr']=''
# print(Program.__dict__)
# Program.__dict__['version']=4.0
# print(Program.__dict__)
print(Program.__dict__['language'] is not None)