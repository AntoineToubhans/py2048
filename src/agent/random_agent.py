import random

from src.game import Action
from .agent_abc import AbstractAgent


class RandomAgent(AbstractAgent):
    @staticmethod
    def get_action_probabilities(state, available_actions):
        """
        Args:
            state (np.array): current observable state
            available_actions (list[src.game.Action]): the list of available actions.

        Returns:
            Dict[src.game.Action, float]: probabilities for each actions.
        """
        chosen_action = random.choice(available_actions)

        return {action: 1 if action is chosen_action else 0 for action in Action}
