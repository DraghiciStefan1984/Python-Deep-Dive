

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    """
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width
    
    def area(self):
        return self.width * self.height
    """

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return "Rectangle: width={0}, height={1}".format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
print(r1)
print(r1.area())
print(r1.perimeter())

r2 = Rectangle(10, 20)

print(r1 is r2)
print(r1 == r2)