""" A module implementing the 2048 AI from https://fabdev.fr/articles/2048-ai/

    The authors claim it is a Monte Carlo tree seach, but I doubt it.
    The idea is to run ~100 random games from the current states for each available action
    and to select the action that leads to the best average score.

    The agent does not store any information between consecutive steps, it is "stateless".
    It does roughly 400 game full explorations at each step which can be time consuming.
"""
from multiprocessing import Pool

from src.game import Action
from src.agent import RandomAgent
from src.agent.agent_abc import AbstractAgent

from .modifiable_game_manager import ModifiableGameManager


class SimpleMonteCarloTreeSearchAgent(AbstractAgent):
    def __init__(self, number_of_run=100):
        """
        Args:
            number_of_run (int): number of run to average the score. Defaults to 100.
        """
        self._number_of_run = number_of_run
        self._random_agent = RandomAgent()

    def get_action_probabilities(self, state, available_actions):
        """
        Args:
            state (np.array): current observable state
            available_actions (list[src.game.Action]): the list of available actions.

        Returns:
            Dict[src.game.Action, float]: probabilities for each actions.
        """
        with Pool(4) as pool:
            average_scores = pool.starmap(
                self._execute_many_games_from_state,
                [(state, action) for action in available_actions],
            )

        average_score_per_action = dict(zip(available_actions, average_scores))
        normalization_factor = sum(average_scores)

        return {
            action: average_score_per_action.get(action, 0) / normalization_factor
            for action in Action
        }

    def _execute_many_games_from_state(self, initial_state, initial_action):
        """ Execute many games starting with the initial action from the given input initial state.

        Args:
            initial_state (np.ndarray): the initial state, a (4, 4) grid
            initial_action (src.game.Action): the first action

        Returns:
            int: the average total score.
        """
        sum_score = sum(
            [
                self._execute_one_game_from_state(
                    initial_state=initial_state, initial_action=initial_action
                )
                for _ in range(self._number_of_run)
            ]
        )

        return sum_score / self._number_of_run

    def _execute_one_game_from_state(self, initial_state, initial_action):
        """ Execute the initial action from the initial state, then executes random actions
            till the end of the game and returns the total score.

        Args:
            initial_state (np.ndarray): the initial state, a (4, 4) grid
            initial_action (src.game.Action): the first action

        Returns:
            int: the total score.
        """
        game_manager = ModifiableGameManager(initial_state=initial_state)
        game_manager.play(initial_action)

        while not game_manager.is_game_over():
            state = game_manager.get_state()
            available_action = game_manager.get_available_actions()

            action_probabilities = self._random_agent.get_action_probabilities(
                state, available_action
            )
            action = max(action_probabilities, key=action_probabilities.get)

            game_manager.play(action)

        return game_manager.score
