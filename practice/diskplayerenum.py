from enum import Enum, auto

class State(Enum):
    EMPTY = auto()
    STOPPED = auto()
    PAUSED = auto()
    PLAYING = auto()

