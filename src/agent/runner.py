from src.game import GameManager
from src.utils.timer import timeit

from .agent_trace import AgentTrace


def run_agent(agent):
    """ Run an agent thru a game from start to the end (game over)

    Args:
        agent (src.agent.AbstractAgent): the agent

    returns:
        src.agent.runner.RunAgentTrace: the list of (state, action, reward) triples
    """
    game_manager = GameManager()

    timed_agent_get_action_probabilities = timeit(agent.get_action_probabilities)
    run_agent_trace = AgentTrace()

    while not game_manager.is_game_over():
        state = game_manager.get_state()
        available_action = game_manager.get_available_actions()

        (
            action_compute_time,
            action_probabilities,
        ) = timed_agent_get_action_probabilities(state, available_action)
        action = max(action_probabilities, key=action_probabilities.get)

        reward = game_manager.play(action)

        run_agent_trace.append(
            state, action_probabilities, action, reward, action_compute_time
        )

    run_agent_trace.set_final_state(game_manager.get_state())

    return run_agent_trace
