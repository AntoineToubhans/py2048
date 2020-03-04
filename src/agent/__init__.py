from .random_agent import RandomAgent
from .mcts.simple_mcts_agent import SimpleMonteCarloTreeSearchAgent


AGENTS = [
    SimpleMonteCarloTreeSearchAgent,
    RandomAgent,
]
