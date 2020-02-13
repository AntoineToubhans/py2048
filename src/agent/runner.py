from src.game import GameManager


class RunAgentTrace:
    def __init__(self):
        self.states = []
        self.actions = []
        self.rewards = []

    def append(self, state, action, reward):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)


def run_agent(agent):
    """ Run an agent thru a game from start to the end (game over)

    Args:
        agent (src.agent.AbstractAgent): the agent

    returns:
        src.agent.runner.RunAgentTrace: the list of (state, action, reward) triples
    """
    game_manager = GameManager()

    run_agent_trace = RunAgentTrace()

    while not game_manager.is_game_over():
        state = game_manager.get_state()
        available_action = game_manager.get_available_actions()

        action = agent.choose_action(state, available_action)

        reward = game_manager.play(action)

        run_agent_trace.append(state, action, reward)

    return run_agent_trace
