import click
from elasticsearch_dsl import connections
import git
from loguru import logger
from tqdm import tqdm

from src.agent import AGENTS
from src.agent.agent_document import AgentDocument
from src.agent.agent_trace_document import (
    AgentTraceDocument,
    AgentTraceTransitionDocument,
)
from src.agent.runner import run_agent


# TODO: put this in a global config
connections.create_connection(hosts=["localhost"], timeout=20)
AgentDocument.init()


def retrieve_agent(agent_name):
    try:
        agent_class = next(agent for agent in AGENTS if agent.__name__ == agent_name)
    except StopIteration:
        logger.error(f"Agent '{agent_name}' not found")
        raise Exception(f"Agent '{agent_name}' not found")

    return agent_class()


def find_or_create_agent_in_es(agent_name):
    commit_sha = git.Repo(search_parent_directories=True).head.object.hexsha
    logger.info(f"Searching for Agent<name={agent_name}, commit_sha={commit_sha}")

    results = (
        AgentDocument.search()
        .filter("match", name=agent_name)
        .filter("match", commit_sha=commit_sha)
        .execute()
    )

    if results.hits.total.value > 1:
        raise Exception("More than one agent exists in ES: agent index is corrupted")

    if results.hits.total.value == 1:
        agent_id = results.hits[0].meta.id
        logger.info(f"Agent found: ID is {agent_id}")
    else:
        logger.info("Agent not found: creating one")
        agent_document = AgentDocument(name=agent_name, commit_sha=commit_sha)
        agent_document.save()
        agent_id = agent_document.meta.id
        logger.info(f"Agent created in ES: ID is {agent_id}")

    return agent_id


@click.option(
    "-a", "--agent-name", required=True, help="Name of the agent (class_name)",
)
@click.option(
    "-n", "--number-of-run", default=1000, help="Number of run",
)
@click.command()
def evaluate_agent(agent_name, number_of_run):
    logger.info(f"Evaluating agent {agent_name}")
    logger.info(f"Number of run: {number_of_run}")

    agent = retrieve_agent(agent_name)
    agent_id = find_or_create_agent_in_es(agent_name)

    for _ in tqdm(range(number_of_run)):
        trace = run_agent(agent)

        trace_document = AgentTraceDocument.from_agent_trace(agent_id, trace)
        trace_document.save()

        for transition_index, transition_dict in enumerate(trace):
            AgentTraceTransitionDocument.from_transition(
                trace_document.meta.id, transition_index, transition_dict,
            ).save()


if __name__ == "__main__":
    evaluate_agent()
