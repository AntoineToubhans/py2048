import abc


class AbstractAgent(abc.ABC):
    @abc.abstractmethod
    def get_parameters(self):
        """ Returns a dictionary containing all agent parameters.

        Returns:
              Dict: the agent parameters.
        """

    @abc.abstractmethod
    def get_action_probabilities(self, state, available_actions):
        """
        Args:
            state (np.array): current observable state
            available_actions (list[src.game.Action]): the list of available actions.

        Returns:
            Dict[src.game.Action, float]: probabilities for each actions.
        """
