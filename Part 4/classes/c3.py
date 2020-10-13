class Person:
    def __init__(self, name):
        # self._name=name
        self.set_name(name)
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._name=value.strip()
        else:
            raise ValueError('Name must of type string.')       
        
        
p=Person('Paul') 
print(p.get_name()) 


class Person:
    def __init__(self, name):
        self._name=name
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._name=value.strip()
        else:
            raise ValueError('Name must of type string.')
        
    name=property(fget=get_name, fset=set_name)
    
    
p=Person('John')
print(p.name)
p.name='Michael'
print(p.name)


class Person:
    def __init__(self, name):
        self._name=name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._name=value.strip()
        else:
            raise ValueError('Name must of type string.')
        

p=Person('Anna')
print(p.name)
p.name='Marry'
print(p.name)