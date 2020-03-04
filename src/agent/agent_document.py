import hashlib

from elasticsearch_dsl import (
    Document,
    Keyword,
    Object,
)
from loguru import logger
import git


class AgentDocument(Document):
    name = Keyword()
    commit_sha = Keyword()
    parameters = Object()
    parameters_hash = Keyword()

    class Index:
        name = "agents"


def _hash_parameters(agent_parameters):
    sha = hashlib.sha256()
    sha.update(str(agent_parameters).encode())

    return sha.hexdigest()


def get_agent_id(agent):
    """ Get agent ID in elasticsearch. Search for an agent with the same 1/ name 2/ parameters 3/ commit sha.
        If no agent is found in elasticsearch, then it is created.

    Args:
        agent (src.agent.agent_abs.AbstractAgent): the agent

    Return:
        str: the ID of the agent in elasticsearch.
    """
    AgentDocument.init()

    agent_name = agent.__class__.__name__
    agent_parameters = agent.get_parameters()
    agent_parameters_hash = _hash_parameters(agent_parameters)
    commit_sha = git.Repo(search_parent_directories=True).head.object.hexsha
    logger.info(
        f"Searching for Agent<name={agent_name}, parameters= {agent_parameters}, commit_sha={commit_sha}"
    )
    results = (
        AgentDocument.search()
        .filter("match", name=agent_name)
        .filter("match", commit_sha=commit_sha)
        .filter("match", parameters_hash=agent_parameters_hash)
        .execute()
    )

    if results.hits.total.value > 1:
        raise Exception("More than one agent exists in ES: agent index is corrupted")

    if results.hits.total.value == 1:
        agent_id = results.hits[0].meta.id
        logger.info(f"Agent found: ID is {agent_id}")
    else:
        logger.info("Agent not found: creating one")
        agent_document = AgentDocument(
            name=agent_name,
            commit_sha=commit_sha,
            parameters=agent_parameters,
            parameters_hash=agent_parameters_hash,
        )
        agent_document.save()
        agent_id = agent_document.meta.id
        logger.info(f"Agent created in ES: ID is {agent_id}")

    return agent_id
