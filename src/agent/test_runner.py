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
    assert type(trace_description["mean_compute_action_time"]) == float
    assert type(trace_description["action_ratio"]) == dict

    assert type(trace_description["action_ratio"]["LEFT"]) == float
    assert type(trace_description["action_ratio"]["RIGHT"]) == float
    assert type(trace_description["action_ratio"]["UP"]) == float
    assert type(trace_description["action_ratio"]["DOWN"]) == float


def test_get_item():
    last_trace_item = trace[-1]

    assert type(last_trace_item["action"]) == Action
    assert type(last_trace_item["reward"]) == np.int64
    assert type(last_trace_item["action_compute_time"]) == float
    assert type(last_trace_item["states"]) == dict
    assert type(last_trace_item["states"]["before_action"]) == np.ndarray
    assert type(last_trace_item["states"]["after_action"]) == np.ndarray

    assert last_trace_item["states"]["before_action"].shape == (4, 4)
    assert last_trace_item["states"]["after_action"].shape == (4, 4)
