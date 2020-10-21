class Person:
    # a class is callable only if we implement the __call__ method
    def __call__(self):
        print('__call__ called')
        
p=Person()
p()


def my_func(a, b, c):
    return a, b, c

class Partial:
    def __init__(self, func, *args):
        self._func=func
        self._args=args
        
    def __call__(self, *args):
        return self._func(*self._args, *args)
    
partial_func=Partial(my_func, 20, 30)
print(partial_func(10))


import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

class Person:
    def __init__(self, name):
        self.name=name
        
    def __repr__(self):
        return f'Person({self.name})'
    
    def __del__(self):
        print(f'__del__ called on {self}...')
        
p=Person('Alex')
print(ref_count(id(p)))

# p=None
del p
print(ref_count(id(p)))