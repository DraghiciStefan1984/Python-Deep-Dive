class Person:
    def __init__(self, name, age):
        self.age=age
        self.name=name
        
    # str for developers, used to return a more detailed
    # representation of the object  
    def __repr__(self):
        print('__repr__ called')
        return f'Person({self.name}, {self.age})'
    
    def __str__(self):
        print('__str__ called')
        return f'{self.name} is {self.age} years old.'
    
    
p=Person('Stefan', 36)
print(p)
print(repr(p))