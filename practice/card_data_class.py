from dataclasses import dataclass, field
from typing import Tuple
from random import sample

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


def make_french_card():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(
            self.suit
        )

    def __str__(self):
        return f"{self.suit}{self.rank}"


@dataclass(frozen=True)
class Deck:
    cards: Tuple[PlayingCard] = field(default_factory=make_french_card)

    def __repr__(self):
        cards = ", ".join(f"{c!s}" for c in self.cards)
        return f"{self.__class__.__name__}({cards})"


# j = PlayingCard(rank='J', suit='♠')
# d = Deck()
# d1 = Deck()
# print(d)
# print(d1)
# print(d.cards.remove(j))
# print("*" * 100)
# print(d)
# print(d1)

deck = Deck(sorted(make_french_card()))
print(deck)

# queen_of_hearts = PlayingCard('Q', '♡')
# ace_of_spades = PlayingCard('A', '♠')

# print(ace_of_spades > queen_of_hearts)
# print(ace_of_spades.sort_index)
# print(queen_of_hearts.sort_index)

p1 = Deck(sample(make_french_card(), k=10))
print(type(p1))
print(p1)
