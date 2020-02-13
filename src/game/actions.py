from enum import Enum, auto


class Action(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def __str__(self):
        return self.name
