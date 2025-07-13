from dataclasses import dataclass
from typing import Any
from dataclasses import field
@dataclass
class Position:
    name:Any
    lon: float = 0.0
    lat: float = 0.0

pos = Position('Oslo',10.8,59.9)
print(pos)
london_pos = Position(43)
print(london_pos)

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False,repr=False)
    rank: str
    suit:str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))
        
    def __str__(self):
        return f"{self.rank}{self.suit}"