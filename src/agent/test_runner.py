import numpy as np

from src.agent.random_agent import RandomAgent
from src.agent.runner import run_agent


random_agent = RandomAgent()
trace = run_agent(random_agent)


def test_describe_types():
    trace_description = trace.describe()

    assert type(trace_description['length']) == int
    assert type(trace_description['score']) == np.int64
    assert type(trace_description['max_tile']) == np.int64
    assert type(trace_description['mean_compute_action_time']) == np.float64
    assert type(trace_description['LEFT_action_ratio']) == np.float64
    assert type(trace_description['RIGHT_action_ratio']) == np.float64
    assert type(trace_description['UP_action_ratio']) == np.float64
    assert type(trace_description['DOWN_action_ratio']) == np.float64
