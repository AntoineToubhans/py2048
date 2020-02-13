from .actions import Action
from .grid import Grid
from .reward import Reward


class GameManager:
    def __init__(self):
        self.score = 0
        self._grid = Grid()

        self._grid.add_random_tile()
        self._grid.add_random_tile()

    def get_state(self):
        return self._grid.values

    def is_game_over(self):
        """
        Returns:
            bool: True iff the game is over
        """
        return not self._grid.has_free_cells_available() and not self._grid.has_tile_matches()

    def get_available_actions(self):
        """
        Returns:
            list[src.game.Action]: the list of available actions
        """
        return [
            action
            for action in Action
            if self._grid.can_move(direction=action)
        ]

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

        return Reward(score=score, tiles_moved=moved)
