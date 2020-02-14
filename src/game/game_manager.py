from .actions import Action
from .exceptions import NotPossibleActionException
from .grid import Grid


class GameManager:
    def __init__(self):
        self.score = 0
        self._grid = Grid()

        self._grid.add_random_tile()
        self._grid.add_random_tile()

    def get_state(self):
        """
        Returns:
            np.array: the current grid state for the game
        """
        return self._grid.values

    def is_game_over(self):
        """
        Returns:
            bool: True iff the game is over
        """
        return (
            not self._grid.has_free_cells_available()
            and not self._grid.has_tile_matches()
        )

    def get_available_actions(self):
        """
        Returns:
            list[src.game.Action]: the list of available actions
        """
        return [action for action in Action if self._grid.can_move(direction=action)]

    def play(self, action):
        """ Play a move

        Args:
            action (src.game.Action): move to be made, either UP, RIGHT, DOWN or LEFT

        Returns:
            int: the reward obtained after the action has been taken. It is the score increment
                corresponding to the values of the merged tiles.

        Raises:
            src.game.exceptions.NotPossibleActionException: if the action is not possible
        """
        if not self._grid.can_move(action):
            raise NotPossibleActionException(action=action)

        tiles_moved, score_increment = self._grid.move(action)

        # This assertion should normally always pass
        assert tiles_moved > 0

        self.score += score_increment
        self._grid.add_random_tile()

        return score_increment
