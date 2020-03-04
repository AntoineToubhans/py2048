from loguru import logger

from src.agent import AGENTS


def retrieve_agent(agent_name, agent_parameters=None):
    try:
        agent_class = next(agent for agent in AGENTS if agent.__name__ == agent_name)
    except StopIteration:
        logger.error(f"Agent '{agent_name}' not found")
        raise Exception(f"Agent '{agent_name}' not found")

    agent_parameters = {} if agent_parameters is None else agent_parameters

    return agent_class(**agent_parameters)
