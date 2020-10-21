class Person:
    def __init__(self, name):
        self._name=name
        
    @property
    def name(self):
        return self._name
        
    def __eq__(self, other):
        return isinstance(other, Person) and self.name==other.name
    
    def __repr__(self):
        return f'Person({self.name})'
    
    def __hash__(self):
        return hash(self.name)
    
    def __bool__(self):
        return len(self.name)


p1=Person('Eric')
p2=Person('Vlad')
print(hash(p1))
print(hash(p2))

d={p1:'Eric Name', p2:'Vlad Tepes'}
print(d)
