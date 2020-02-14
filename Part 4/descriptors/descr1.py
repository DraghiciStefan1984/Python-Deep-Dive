# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:32:17 2020

@author: Stefan Draghici
"""

from datetime import datetime
from random import choice, seed


class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat
    
class Logger:
    current_time=TimeUTC()
    
#test
l=Logger()
print(l.current_time())


'''
class Deck:
    @property
    def suit(self):
        return choice(('Spade', 'Heart', 'Diamond', 'Club'))
    
    @property
    def card(self):
        return choice(tuple('23456789JKQA')+('10',))
'''
 
#the Choice descriptor
class Choice:
    def __init__(self, *choices):
        self.choices=choices
        
    def __get__(self, instance, owner_class):
        return choice(self.choices)
    
class Deck:
    suit=Choice('Spade', 'Heart', 'Diamond', 'Club')
    card=Choice(*'23456789JKQA','10')
    
#test
d=Deck()
for _ in range(10):
    print(d.card, d.suit)