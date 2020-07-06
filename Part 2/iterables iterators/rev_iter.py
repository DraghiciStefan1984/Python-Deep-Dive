from collections import  namedtuple


_SUITS=('Spades', 'Hearts', 'Diamonds', 'Clubs')
_RANKS=(tuple(range(2, 11))+tuple('JQKA'))

Card=namedtuple('Card', 'rank suit')

class CardDeck:
    def __init__(self):
        self.length=len(_SUITS)*len(_RANKS)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    def __reversed__(self):
        return self.CardDeckIterator(self.length)

    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length=length
            self.reverse=reverse
            self.i=0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i>=self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index=self.length-1-self.i
                else:
                    index=self.i
                suit=_SUITS[index//len(_RANKS)]
                rank=_RANKS[index%len(_RANKS)]
                self.i+=1
                return Card(rank, suit)


# deck=CardDeck()
# for card in deck:
#     print(card)

deck=reversed(CardDeck())
for card in deck:
    print(card)


class Squares:
    def __init__(self, length):
        self.squares=[i**2 for i in range(length)]

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, s):
        return self.squares[s]