from src.game import Action
from .exceptions import (
    AgentTraceFinalStateNotSetError,
    AgentTraceFinalStateAlreadySetError,
)


class AgentTrace:
    """ Agent Trace
    An agent trace is a list of the form [s0, a0, r0, s1, a1, r1, ..., sN, aN, rN, sFinal] where:
        - s0, ..., sN, sFinal are states
        - a0, ..., aN are actions
        - r0, ..., rN are rewards
    Given a state sN, an agent chooses an action aN that will give a reward sN and the next state sN+1.
    """

    def __init__(self):
        self._states = []
        self._action_probabilities = []
        self._actions = []
        self._rewards = []
        self._action_compute_times = []
        self._final_state = None

    def append(
        self, state, action_probabilities, chosen_action, reward, action_compute_time
    ):
        """ Add a transition to an agent trace.

        Args:
            state (numpy.ndarray): a state
            action_probabilities (Dict[src.game.Action, float]: probabilities per action
            chosen_action (src.game.Action): the action chosen by the agent
            reward (int): the reward following the action
            action_compute_time (float): time for the agent to compute the action
        Raises:
            AgentTraceFinalStateAlreadySetError: raised if the final state has already be set.
        """
        if self._final_state is not None:
            raise AgentTraceFinalStateAlreadySetError

        self._states.append(state)
        self._action_probabilities.append(action_probabilities)
        self._actions.append(chosen_action.value)
        self._rewards.append(reward)
        self._action_compute_times.append(action_compute_time)

    def set_final_state(self, state):
        """ Set the final (gameover) state

        Args:
            state (numpy.ndarray): the final state
        Raises:
            AgentTraceFinalStateAlreadySetError: raised if the final state has already be set.
        """
        if self._final_state is not None:
            raise AgentTraceFinalStateAlreadySetError

        self._final_state = state

    def __getitem__(self, item):
        if self._final_state is None:
            # Data should not be retrieved while final state has not been set
            raise AgentTraceFinalStateNotSetError

        return {
            "state_before_action": self._states[item],
            "action": Action(self._actions[item]),
            "action_probabilities": self._action_probabilities[item],
            "reward": self._rewards[item],
            "action_compute_time": self._action_compute_times[item],
            "state_after_action": self._final_state
            if item + 1 == len(self) or item == -1
            else self._states[item + 1],
        }

    def __len__(self):
        return len(self._states)

    def describe(self):
        if self._final_state is None:
            # Data should not be retrieved while final state has not been set
            raise AgentTraceFinalStateNotSetError

        trace_length = len(self)

        return {
            "length": trace_length,
            "max_tile": self._states[-1].max(),
            "score": sum(self._rewards),
            "mean_compute_action_time": sum(self._action_compute_times) / trace_length,
            "action_ratio": {
                action.name: self._actions.count(action.value) / trace_length
                for action in Action
            },
        }
