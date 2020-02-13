import numpy as np

from .constants import BOARD_SIZE
from .grid import Grid
from .reward import Reward


class GameManager:
    def __init__(self):
        self.game_over = False
        self.score = 0
        self._grid = Grid()

        self._grid.add_random_tile()
        self._grid.add_random_tile()

    def get_state(self):
        return self._grid.values

    def can_move(self, direction):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE - 1):
                value = self._grid.get(i, j, direction=direction)
                next_value = self._grid.get(i, j + 1, direction=direction)
                if value != 0 and value == next_value:
                    return True
                elif value == 0 and next_value != 0:
                    return True

        return False

    def has_tile_match_available(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE - 1):
                if self._grid.get(i, j) == self._grid.get(i, j + 1) and self._grid.get(i, j) != 0:
                    return True
                if self._grid.get(j, i) == self._grid.get(j + 1, i) and self._grid.get(j, i) != 0:
                    return True

        return False

    def has_move_available(self):
        return self._grid.has_cells_available() or self.has_tile_match_available()

    def play(self, action):
        """ Play a move

        Args:
            action (src.game.Action): move to be made, either UP, RIGHT, DOWN or LEFT

        Returns:
            src.game.Reward: the reward obtained after the action has been taken

        Raises:
            src.game.exceptions.ActionNotPossibleException: if the action is not possible
        """
        moved, score = self._grid.move(action)
        self.score += score

        if moved:
            self._grid.add_random_tile()

            if not self.has_move_available():
                self.game_over = True
            
        return Reward(score=score, tiles_moved=moved)
