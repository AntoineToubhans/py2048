import numpy as np

from src.game import Action
from src.game.constants import BOARD_SIZE
from src.game.exceptions import NoFreeCellError


POSITION_TURNS = {
    Action.UP: lambda i, j: (j, i),
    Action.RIGHT: lambda i, j: (i, BOARD_SIZE - j - 1),
    Action.DOWN: lambda i, j: (BOARD_SIZE - j - 1, i),
    Action.LEFT: lambda i, j: (i, j),
}


def _convert_power_two(value):
    return 2 ** value if value > 0 else 0


class Grid:
    """ Grid for 2048 game. """

    def __init__(self):
        self._grid = np.zeros((BOARD_SIZE, BOARD_SIZE)).astype(np.uint8)

    @property
    def values(self):
        return np.vectorize(_convert_power_two)(self._grid)

    def _get(self, i, j, direction=None):
        if direction is not None:
            i, j = POSITION_TURNS[direction](i, j)
        return self._grid[i][j]

    def _set(self, i, j, value, direction=None):
        if direction is not None:
            i, j = POSITION_TURNS[direction](i, j)
        self._grid[i][j] = value

    def _get_available_cells(self):
        return np.argwhere(self._grid == 0)

    def _get_random_available_cell(self):
        cells = self._get_available_cells()

        if len(cells) == 0:
            raise NoFreeCellError("No available cell :/")

        return cells[int(np.random.random() * len(cells))]

    def has_free_cells_available(self):
        return self._grid.min() == 0

    def has_tile_matches(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE - 1):
                if self._get(i, j) == self._get(i, j + 1) and self._get(i, j) != 0:
                    return True
                if self._get(j, i) == self._get(j + 1, i) and self._get(j, i) != 0:
                    return True

        return False

    def can_move(self, direction):
        """
        Args:
            direction (src.game.Action): an action
        Returns:
            bool: True if the action is possible i.e. if it moves tiles
        """
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE - 1):
                value = self._get(i, j, direction=direction)
                next_value = self._get(i, j + 1, direction=direction)
                if value != 0 and value == next_value:
                    return True
                elif value == 0 and next_value != 0:
                    return True

        return False

    def add_random_tile(self):
        value = 1 if np.random.random() < 0.9 else 2

        i, j = self._get_random_available_cell()

        self._set(i, j, value)

    def move(self, direction):
        score = np.int64(0)
        moved = 0

        # Collapse & merge
        for i in range(BOARD_SIZE):
            offset = 0
            collapse_value = None

            for j in range(BOARD_SIZE):
                value = self._get(i, j, direction=direction)
                if value == 0:
                    offset += 1
                elif value == collapse_value:
                    new_value = value + 1

                    self._set(i, j, 0, direction=direction)
                    self._set(i, j - offset - 1, new_value, direction=direction)
                    offset += 1
                    collapse_value = None

                    score += _convert_power_two(new_value)
                    moved += 1
                elif offset > 0:
                    self._set(i, j, 0, direction=direction)
                    self._set(i, j - offset, value, direction=direction)
                    collapse_value = value

                    moved += 1
                else:
                    collapse_value = value

        return moved, score
