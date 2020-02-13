import random

from .agent_abc import AbstractAgent


class RandomAgent(AbstractAgent):
    @staticmethod
    def choose_action(state, available_actions):
        """
        Args:
            state (np.array): current observable state
            available_actions (list[src.game.Action]): the list of available actions.

        Returns:
            action (src.game.Action): the action the agent choose to play
        """
        return random.choice(available_actions)
