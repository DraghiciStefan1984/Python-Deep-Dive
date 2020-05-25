class Rectangle:
    def __init__(self, width, height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value<=0:
            raise ValueError('width cannot be negative')
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value<=0:
            raise ValueError('height cannot be negative')
        self._height=value

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*self.width+2*self.height

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __repr__(self):
        return 'Rectangle - width: ({0}) - height: ({1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width==other.width and self.height==other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area()<other.area()
        else:
            return NotImplemented


r=Rectangle(23, 45)
print(r.width)
print(r.height)
print(r.area())
print(r.perimeter())
print(r)
print(r.__repr__())

r2=Rectangle(23, 42)
print(r==r2)
print(r<r2)