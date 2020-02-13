import numpy as np

from src.game import Action


class RunAgentTrace:
    def __init__(self):
        self._states = []
        self._actions = []
        self._rewards = []
        self._action_compute_times = []
        self.final_state = None

    def append(self, state, action, reward, action_compute_time):
        self._states.append(state)
        self._actions.append(action.value)
        self._rewards.append(reward)
        self._action_compute_times.append(action_compute_time)

    def set_final_state(self, state):
        self.final_state = state

    @property
    def states(self):
        return np.stack(self._states)

    @property
    def actions(self):
        return np.stack(self._actions)

    @property
    def rewards(self):
        return np.stack(self._rewards)

    @property
    def action_compute_times(self):
        return np.stack(self._action_compute_times)

    def __getitem__(self, item):
        return {
            'state': self.states[item],
            'action': Action(self.actions[item]),
            'reward': self.rewards[item],
            'action_compute_time': self.action_compute_times[item],
        }

    def __len__(self):
        return len(self.states)

    def describe(self):
        trace_length = len(self)

        action_description = {
            f'{action.name}_action_ratio':
                (self.actions == action.value).sum() / trace_length
            for action in Action
        }

        return {
            'length': trace_length,
            'max_tile': self.final_state.max(),
            'score': self.rewards.sum(),
            'mean_compute_action_time': self.action_compute_times.mean(),
            **action_description,
        }
