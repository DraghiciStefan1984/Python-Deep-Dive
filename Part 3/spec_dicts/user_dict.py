from number import Real


class IntDict1:
    def __init__(self):
        self._d={}
        
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('value must be a real number')
        self._d[key]=value
        
    def __getitem__(self, key):
        return int(self._d[key])
    
    
class IntDict2(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('value must be a real number')
            super().__setitem__(key, value)
            
    def __getitem__(self, key):
        return super().__getitem__(key)