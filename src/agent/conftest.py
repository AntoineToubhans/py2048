import numpy as np
import pytest

from src.game import Action
from .agent_trace import AgentTrace


@pytest.fixture()
def state0():
    return np.zeros((4, 4)).astype(np.uint8)


@pytest.fixture()
def state1():
    return np.ones((4, 4)).astype(np.uint8) * 2


@pytest.fixture()
def state2():
    return np.ones((4, 4)).astype(np.uint8) * 4


@pytest.fixture()
# pylint: disable=redefined-outer-name
def trace(state0, state1):
    agent_trace = AgentTrace()
    agent_trace.append(
        action_compute_time=1.234,
        state=state0,
        action_probabilities={
            Action.UP: 1,
            Action.DOWN: 0,
            Action.LEFT: 0.2,
            Action.RIGHT: 0,
        },
        chosen_action=Action.UP,
        reward=666,
    )
    agent_trace.append(
        action_compute_time=2.345,
        state=state1,
        action_probabilities={
            Action.UP: 0,
            Action.DOWN: 1,
            Action.LEFT: 0.2,
            Action.RIGHT: 0,
        },
        chosen_action=Action.DOWN,
        reward=42,
    )

    return agent_trace
