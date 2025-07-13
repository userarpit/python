import random
from typing import List, Tuple, Sequence, TypeVar, Optional

Card = Tuple[str, str]
Deck = List[Card]
Choosable = TypeVar("Choosable", str, Card)

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def create_deck(shuffle: bool = False) -> List[Card]:

    deck = [(s, r) for s in SUITS for r in RANKS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:

    # print(deck[0::4])
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


def choose(players: Sequence[Choosable]) -> Choosable:
    return random.choice(players)


def player_order(players: Sequence[str], start: Optional[str] = None) -> List[str]:
    if start is None:
        start = choose(players)
    start_idx = players.index(start)
    return players[start_idx:] + players[:start_idx]


def play() -> None:
    deck = create_deck(shuffle=True)

    players = "P1 P2 P3 P4".split()
    cards = deal_hands(deck)

    hands = {p: c for p, c in zip(players, cards)}
    # print(hands)
    for k, v in hands.items():
        player_cards = " ".join(f"{s}{r}" for (s, r) in v)
        print(f"{k}: {player_cards}")

    start_player = choose(players)
    print(type(start_player))
    turn_order = player_order(players, start=start_player)

    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            # print(type(card))
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<4}  ", end="")
        print()

    # print(hands[start_player])


if __name__ == "__main__":
    play()
