import numpy as np
import pytest
from pytest_cov.embed import cleanup_on_sigterm

from src.agent import RandomAgent, SimpleMonteCarloTreeSearchAgent
from src.game import Action

# This allows coverage to track code run in subprocesses
# https://pytest-cov.readthedocs.io/en/v2.8.1/subprocess-support.html
cleanup_on_sigterm()


@pytest.fixture()
def initial_state():
    # Returns an initial state for which Action.UP is not possible
    return np.array([[0, 2, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])


@pytest.mark.parametrize(
    "agent", [RandomAgent(), SimpleMonteCarloTreeSearchAgent(number_of_run=10),]
)
def test_agent_returns_action_probabilities(initial_state, agent):
    action_probabilities = agent.get_action_probabilities(
        initial_state, [Action.LEFT, Action.RIGHT, Action.DOWN,]
    )

    assert len(action_probabilities) == 4
    assert sum(action_probabilities.values()) == pytest.approx(1)

    for action in Action:
        assert action in action_probabilities
        assert action_probabilities[action] >= 0
        assert action_probabilities[action] <= 1

    assert action_probabilities[Action.UP] == 0
