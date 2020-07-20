
class Person:
    def __init__(self, name):
        # self._name=name
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._name=value.strip()
        else:
            raise ValueError('name must be a valid, non-empty string')

    name=property(fget=get_name, fset=set_name)


p=Person('alex')
# p.name=7
print(p.name)


class Person:
    def __init__(self, name):
        self._name=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._name=value.strip()
        else:
            raise ValueError('name must be a valid, non-empty string')


p=Person('')
print(p.name)