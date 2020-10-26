from app.utils.validators import validate_integer


class Resource:
    """Base class for resources"""
    
    def __init__(self, name, manufacturer, total, allocated):
        """
        Args:
            name (str): name of resource
            manufacturer (str): name of manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
        """
        
        self._name=name
        self._manufacturer=manufacturer
        
        validate_integer('total', total, min_value=0)
        self._total=total
        
        validate_integer('allocated', 
                         allocated, 
                         min_value=0, 
                         max_value=total,
                         custom_max_message='Allocated inventory cannot exceed total inventory')
        self._allocated=allocated
        
    @property
    def name(self):
        return self._name
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @property
    def total(self): 
        return self._total
    
    @property
    def allocated(self): 
        return self._allocated
    
    @property
    def category(self): 
        """
        Returns:
            str: resource category in lower case
        """
        return type(self).__name__.lower()
    
    @property
    def available(self):
        return self.total-self.allocated
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return (f'{self.name ({self.category - self.manufacturer}): total={self.total}, allocated={self.allocated}}')
    
    def claim(self, num):
        validate_integer('num', 
                         num, 
                         1, 
                         self.available, 
                         custom_max_message=f'Cannot claim more than {self.available}.')
        self._allocated+=num
        
    def freeup(self, num):
        validate_integer('num', 
                         num, 
                         1, 
                         self.available, 
                         custom_max_message=f'Cannot return more than {self.available}.')
        self._allocated-=num
    
    def dies(self, num):
        validate_integer('num', 
                         num, 
                         1, 
                         self.allocated, 
                         custom_max_message=f'Cannot retire more than {self.allocated}.')
        self._total-=num
        self._allocated-=num
    
    def purchased(self, num):
        validate_integer('num', num, 1)
        self._total+=num


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, 
                 cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        
        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)
        self._cores=cores
        self._power_watts=power_watts
        self._socket=socket
        
    @property
    def cores(self):
        return self._cores
    
    @property
    def power_watts(self):
        return self._power_watts
    
    @property
    def socket(self):
        return self._socket
    
    def __repr__(self):
        return f'{self.category}: {self.name} ({self.socket}-x{self.cores})'
        