class Location:
    __slots__='name', '_longitude', '_latitude'
    
    def __init__(self, name, longitude, latitude):
        self._longitude=longitude
        self._latitude=latitude
        self.name=name
        
    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude
    
    
print(Location.__dict__)
l=Location('Bucharest', longitude=45.565, latitude=23.3232)
#print(l.__dict__) #doesn't work because Location instance has slots instead of dict

del l.name
#del l.longitude #properties cannot be deleted


class Person:
    __slots__='name',
    
    def __init__(self, name):
        self.name=name
        
class Student(Person):
    __slots__=tuple()


p=Person('Eric')
s=Student('Alex')
# print(s.__dict__)