class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    def work(self):
        result=super().work()
        return f'Student works and... {result}'
        
# p=Person()
# s=Student()
# print(p.work())
# print(s.work())


class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    def work(self):
        result=super().work()
        return f'Student studies and... {result}'

class PythonStudent(Student):
    def work(self):
        result=super().work()
        return f'Python Student codes and... {result}'
    
p=Person()
s=Student()
py=PythonStudent()
print(p.work())
print(s.work())
print(py.work())


class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    def study(self):
        return f'Student studies...'

class PythonStudent(Student):
    def code(self):
        return f'Python Student codes...'
    
p=Person()
s=Student()
py=PythonStudent()
print(p.work())
print(s.study())
print(py.code())