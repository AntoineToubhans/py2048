from enum import Enum, auto


class Action2048(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def __str__(self):
        return self.name
