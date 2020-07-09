def squares_gen(n):
    for i in range(n):
        yield i**2

sq=squares_gen(10)
for num in sq:
    print(num)

for num in squares_gen(10):
    print(num)


class Squares:
    def __init__(self, n):
        self.n=n

    def __iter__(self):
        return Squares.squares_gen(self.n)

    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i**2


sq=Squares(10)
print(list(sq))


from collections import namedtuple

Card=namedtuple('Card', 'rank suit')
SUITS=('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS=tuple(range(2, 11))+tuple('JQKA')

def card_gen():
    for i in range(len(SUITS)*len(RANKS)):
        suit=SUITS[i//len(RANKS)]
        rank=RANKS[i%len(RANKS)]
        card=Card(rank, suit)
        yield card

for card in card_gen():
    print(card)


def card_gen():
    for suit in SUITS:
        for rank in RANKS:
            yield Card(rank, suit)

for card in card_gen():
    print(card)


class CardDeck:
    SUITS=('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS=tuple(range(2, 11))+tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_gen()

    @staticmethod
    def card_gen():
        for suit in SUITS:
            for rank in RANKS:
                yield Card(rank, suit)


deck=CardDeck()
print(list(deck))