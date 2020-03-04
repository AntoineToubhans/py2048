import pytest
import numpy as np

from src.game import Action
from .exceptions import (
    AgentTraceFinalStateAlreadySetError,
    AgentTraceFinalStateNotSetError,
)


def test_can_not_access_data_while_final_state_has_not_been_set(trace):
    with pytest.raises(AgentTraceFinalStateNotSetError):
        trace[0]

    with pytest.raises(AgentTraceFinalStateNotSetError):
        trace[1]


def test_can_access_data_when_final_state_has_been_set(state0, state1, state2, trace):
    trace.set_final_state(state2)

    assert (
        trace[0].items()
        >= {"reward": 666, "action": Action.UP, "action_compute_time": 1.234,}.items()
    )

    np.testing.assert_array_equal(trace[0]["state_before_action"], state0)
    np.testing.assert_array_equal(trace[0]["state_after_action"], state1)

    assert (
        trace[1].items()
        >= {"reward": 42, "action": Action.DOWN, "action_compute_time": 2.345,}.items()
    )

    np.testing.assert_array_equal(trace[1]["state_before_action"], state1)
    np.testing.assert_array_equal(trace[1]["state_after_action"], state2)

    assert (
        trace[-1].items()
        >= {"reward": 42, "action": Action.DOWN, "action_compute_time": 2.345,}.items()
    )

    np.testing.assert_array_equal(trace[-1]["state_before_action"], state1)
    np.testing.assert_array_equal(trace[-1]["state_after_action"], state2)


def test_can_not_append_when_final_state_has_been_set(state2, trace):
    trace.set_final_state(state2)

    with pytest.raises(AgentTraceFinalStateAlreadySetError):
        trace.append(
            state=state2,
            reward=32,
            action_probabilities={
                Action.UP: 0,
                Action.DOWN: 1,
                Action.LEFT: 0.2,
                Action.RIGHT: 0,
            },
            chosen_action=Action.DOWN,
            action_compute_time=2.345,
        )


def test_can_not_set_final_state_twice(state2, trace):
    trace.set_final_state(state2)

    with pytest.raises(AgentTraceFinalStateAlreadySetError):
        trace.set_final_state(state2)


def test_can_not_describe_a_trace_if_final_state_is_not_set(trace):
    with pytest.raises(AgentTraceFinalStateNotSetError):
        trace.describe()
