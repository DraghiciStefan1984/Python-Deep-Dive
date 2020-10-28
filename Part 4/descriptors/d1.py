from datetime import datetime
from random import choice, seed


class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.now().isoformat()
    

class Logger:
    current_time=TimeUTC()
    
    
print(Logger.__dict__)
print(Logger.current_time)

l=Logger()
print(l.current_time)


class Deck:
    @property
    def suit(self):
        return choice(('Spade', 'Heart', 'Diamond', 'Club'))
    
    @property
    def card(self):
        return choice(tuple('23456789JQKA')+('10',))
    
    
# seed=0
# d=Deck()
# for _ in range(10):
#     print(d.card, d.suit)

    
# the descriptor class
class Choice:
    def __init__(self, *choices):
        self.choices=choices
        
    def __get__(self, instance, owner_class):
        return choice(self.choices)    
    

class Deck:
    suit=Choice('Spade', 'Heart', 'Diamond', 'Club')
    card=Choice(*'23456789JQKA', '10')
    
class Dice:
    dice_1=Choice(1,2,3,4,5,6)
    dice_2=Choice(1,2,3,4,5,6)
    dice_3=Choice(1,2,3,4,5,6)
    
seed=0
deck=Deck()
dice=Dice()

for _ in range(10):
    print(deck.card, deck.suit)
    
for _ in range(10):
    print(dice.dice_1, dice.dice_2, dice.dice_3)
