import abc


class AbstractAgent(abc.ABC):
    @abc.abstractmethod
    def choose_action(self, state, available_actions):
        """
        Args:
            state (np.array): current observable state
            available_actions (list[src.game.Action]): the list of available actions.

        Returns:
            action (src.game.Action): the action the agent choose to play
        """
