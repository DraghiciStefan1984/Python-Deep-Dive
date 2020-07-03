import math

class Circle:
    def __init__(self, r):
        self.radius=r
        self._area=None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius=r
        self._area=None

    @property
    def area(self):
        if not self._area:
            print('Calculating area...')
            self._area=math.pi*(self.radius**2)
        return self._area


c=Circle(23)
print(c.area)
print(c.radius)
c.radius=13
print(c.area)
c.radius=13
print(c.area)
print(c.area)
print(c.area)


class Factorials:
    def __init__(self, length):
        self.length=length

    def __iter__(self):
        return self.FactIter(self.length)

    class FactIter:
        def __init__(self, length):
            self.length=length
            self.i=0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i>=self.length:
                raise StopIteration
            else:
                result=math.factorial(self.i)
                self.i+=1
                return result


facts=Factorials(8)
print(list(facts))