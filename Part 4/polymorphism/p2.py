from numbers import Real


class Vector:
    def __init__(self, *components):
        if len(components)<1:
            raise ValueError('cannot create and empty Vector')
        for component in components:
            if not isinstance(component, Real):
                raise ValueError('Vector component must all be real numbers')
        self._components=components
        
    def __len__(self):
        return len(self._components)
    
    @propoerty
    def components(self):
        return self._components
    
    def __repr__(self):
        return f'Vector({self.components})'
    
    def validate_type_and_dimension(self, v):
        return isinstance(v, Vector) and len(self)==len(v)
    
    def __add__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented
        components=(x+y for x, y in zip(self.components, other.components))
        return Vector(*components)
    
    def __add__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented
        components=(x-y for x, y in zip(self.components, other.components))
        return Vector(*components)
    
    def __mul__(self, other):
        # scalar multiplication
        if isinstance(other, Real):
            components=(other*x for x in self.components)
            return Vector(*components)
        # dot product
        if self.validate_type_and_dimension(other):
            components=(x*y for x, y in zip(self.components, other.components))
            return sum(components)
        return NotImplemented
    
    def __rmul__(self, other):
        return self*other
    
    def __matmul__(self, other):
        # gets called when we have something like v1 @ v2
        print('__matmul__ called')