import numbers


class IntegerField:
    def __init__(self, min_, max_):
        self._min=min_
        self._max=max_
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name=prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise TypeError(f'{self.prop_name} is not Integral')
        if value<self._min:
            raise ValueError(f'{self.prop_name} is less than {self._min}')
        if value>self._max: 
            raise ValueError(f'{self.prop_name} is greater than {self._max}')
        instance.__dict__[self.prop_name]=value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)