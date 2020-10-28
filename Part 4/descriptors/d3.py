class IntegerValue:
    def __init__(self, name):
        self.storage_name='_'+name
        
    def __set__(self, instance, value):
        # instance.stored_value=int(value)
        setattr(instance, self.storage_name, value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name, None)
        
        
# class Point1D:
#     x=IntegerValue()
    
class Point2D:
    x=IntegerValue('x')
    y=IntegerValue('y')
    
    
# p1, p2=Point1D(), Point1D()
# p1.x=12
# p2.x=22
# print(p1.x, p2.x)


p3, p4=Point2D(), Point2D()
p3.x=12
p3.y=33
p4.x=220
p4.y=123
print(p3.x, p3.y)
print(p4.x, p4.y)


class IntegerValue:
    def __init__(self):
        self.values={}
        
    def __set__(self, instance, value):
        self.values[instance]=int(value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance, None)
        
class Point2D:
    x=IntegerValue()
    y=IntegerValue()
    
p3, p4=Point2D(), Point2D()
p3.x=12
p3.y=33
p4.x=220
p4.y=123
print(p3.x, p3.y)
print(p4.x, p4.y)