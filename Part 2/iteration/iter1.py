# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 08:53:22 2020

@author: Stefan Draghici
"""

import random

#the class is an iterator
class Squares:
    def __init__(self, length):
        self.length=length
        self.i=0
        
    def __len__(self):
        return self.length
        
    def __next__(self):
        if self.i>=self.length:
            raise StopIteration
        else:
            result=self.i**2
            self.i+=1
            return result
        
    def __iter__(self):
        return self
        
        
class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length=length
        self.range_min=range_min
        self.range_max=range_max
        self.num_requested=0
        
    def __len__(self):
        return self.length
    
    def __next__(self):
        if self.num_requested>=self.length:
            raise StopIteration
        else:
            self.num_requested+=1
            return random.randint(self.range_min, self.range_max)
        
        
class Cities:
    def __init__(self):
        self._cities=['Bucuresti', 'Sibiu', 'Cluj', 'Brasov', 'Iasi', 'Sinaia']
        self._index=0
        
    def __len__(self):
        return len(self._cities)
    
    def __iter__(self):
        return self.CityIterator(self)
    
    def __next__(self):
        if self._index>=len(self._cities):
            raise StopIteration
        else:
            item=self._cities[self._index]
            self._index+=1
            return item
        
    def __getitem__(self, s):
        return self._cities[s]
        
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
        
        
#test
s=Squares(10)
for item in s:
    print(item)

cities=Cities()
#city_iterator=CityIterator(cities)
#for city in city_iterator:
for city in cities:
    print(city)




















