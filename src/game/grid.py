import numpy as np

from src.game.constants import BOARD_SIZE
from src.game import Action


POSITION_TURNS = {
    Action.UP: lambda i, j: (j, i),
    Action.RIGHT: lambda i, j: (i, BOARD_SIZE - j - 1),
    Action.DOWN: lambda i, j: (BOARD_SIZE - j - 1, i),
    Action.LEFT: lambda i, j: (i, j),
}


class Grid:
    """ Grid for 2048 game.
    """
    def __init__(self):
        self._grid = np.zeros((BOARD_SIZE, BOARD_SIZE)).astype(np.uint8)

    @property
    def grid(self):
        return self._grid

    def get(self, i, j, direction=None):
        if direction is not None:
            i, j = POSITION_TURNS[direction](i, j)
        return self._grid[i][j]

    def set(self, i, j, v, direction=None):
        if direction is not None:
            i, j = POSITION_TURNS[direction](i, j)
        self._grid[i][j] = v

    def has_cells_available(self):
        return self._grid.min() == 0

    def _get_available_cells(self):
        return [
            (i, j)
            for i, xi in enumerate(self._grid)
            for j, value in enumerate(xi)
            if value == 0
        ]

    def _get_random_available_cell(self):
        cells = self._get_available_cells()

        if len(cells) == 0:
            raise Exception('No available cell :/')

        return cells[int(np.random.random() * len(cells))]

    def add_random_tile(self):
        value = 1 if np.random.random() < 0.9 else 2

        i, j = self._get_random_available_cell()

        self.set(i, j, value)
