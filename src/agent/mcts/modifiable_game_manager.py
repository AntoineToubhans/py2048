""" Modifiable Game Manager

    This module extends the src.game.GameManager class so that it can dynamically set the state and
    make deep copy. This allows exploring different path in parallel which is necessary for MCTS.

    Methods set_state() and copy() are not available in the core GameManager() to ensure these
    capabilities are not used in the agent evaluation process.
"""
from math import log2

import numpy as np

from src.game import GameManager
from src.game.grid import Grid


class ModifiableGrid(Grid):
    def __init__(self, initial_state):
        """
        Args:
            initial_state (np.ndarray): a (4, 4) array representing the initial grid
        """
        super(ModifiableGrid, self).__init__()
        self._grid = np.vectorize(self._convert_value)(initial_state).astype(np.uint8)

    @staticmethod
    def _convert_value(value):
        return 0 if value == 0 else int(log2(value))


class ModifiableGameManager(GameManager):
    def __init__(self, initial_state):
        """
        Args:
            initial_state (np.ndarray): a (4, 4) array representing the initial grid
        """
        super(ModifiableGameManager, self).__init__()
        self._grid = ModifiableGrid(initial_state=initial_state)

    def copy(self):
        """
        Returns:
            ModifiableGameManager: a deep copy of the current game manager
        """
        return ModifiableGameManager(initial_state=self.get_state(),)
