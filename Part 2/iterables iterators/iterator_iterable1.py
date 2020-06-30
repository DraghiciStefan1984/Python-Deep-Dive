class Cities:
    def __init__(self):
        self._cities=['Bucharest', 'Berlin', 'London', 'Rome', 'Paris']
        self._index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index>=len(self._cities):
            raise StopIteration
        else:
            item=self._cities[self._index]
            self._index+=1
            return item

    def __len__(self):
        return len(self._cities)


# using ITERATOR protocol
class CityIterator:
    def __init__(self, city_obj):
        self._city_obj=city_obj
        self._index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index>=len(self._city_obj):
            raise StopIteration
        else:
            item=self._city_obj._cities[self._index]
            self._index+=1
            return item


c=Cities()
print(list(c))
print(list(enumerate(c)))

c=Cities()
print(list(enumerate(c)))


cities=Cities()
for city in cities:
    print(city)


cities=Cities()
ci=CityIterator(cities)
for city in ci:
    print(city)