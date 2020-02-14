import numpy as np

from src.agent.random_agent import RandomAgent
from src.agent.runner import run_agent
from src.game import Action


random_agent = RandomAgent()
trace = run_agent(random_agent)


def test_describe_types():
    trace_description = trace.describe()

    assert type(trace_description["length"]) == int
    assert type(trace_description["score"]) == np.int64
    assert type(trace_description["max_tile"]) == np.int64
    assert type(trace_description["mean_compute_action_time"]) == np.float64
    assert type(trace_description["LEFT_action_ratio"]) == np.float64
    assert type(trace_description["RIGHT_action_ratio"]) == np.float64
    assert type(trace_description["UP_action_ratio"]) == np.float64
    assert type(trace_description["DOWN_action_ratio"]) == np.float64


def test_get_item():
    last_trace_item = trace[-1]

    assert type(last_trace_item["state"]) == np.ndarray
    assert type(last_trace_item["action"]) == Action
    assert type(last_trace_item["reward"]) == np.int64
    assert type(last_trace_item["action_compute_time"]) == np.float64

    assert last_trace_item["state"].shape == (4, 4)
