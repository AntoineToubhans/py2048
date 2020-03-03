import click
from elasticsearch_dsl import connections
from loguru import logger
from tqdm import tqdm

from src.agent.agent_document import get_agent_id
from src.agent.agent_trace_document import (
    AgentTraceDocument,
    AgentTraceTransitionDocument,
)
from src.agent.runner import run_agent
from src.agent.utils import retrieve_agent


# TODO: put this in a global config
connections.create_connection(hosts=["localhost"], timeout=20)


def _format_agent_parameters(raw_agent_parameters):
    def _format_agent_parameter(agent_parameter_str):
        parameter_name, parameter_value = agent_parameter_str.split("=")
        try:
            parameter_value = int(parameter_value)
        except ValueError:
            try:
                parameter_value = float(parameter_value)
            except ValueError:
                pass

        return parameter_name, parameter_value

    return dict(map(_format_agent_parameter, raw_agent_parameters))


@click.option(
    "-a", "--agent-name", required=True, help="Name of the agent (class_name)",
)
@click.option(
    "-p",
    "--agent-parameters",
    multiple=True,
    default=[],
    help="Agent parameters, -p PARAM_NAME=PARAM_VALUE",
)
@click.option(
    "-n", "--number-of-run", default=1000, help="Number of run",
)
@click.command()
def evaluate_agent(agent_name, agent_parameters, number_of_run):
    agent_parameters = _format_agent_parameters(agent_parameters)
    logger.info(f"Evaluating agent {agent_name}")
    logger.info(f"with parameters: {agent_parameters}")
    logger.info(f"Number of run: {number_of_run}")

    agent = retrieve_agent(agent_name, agent_parameters)
    agent_id = get_agent_id(agent)

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
