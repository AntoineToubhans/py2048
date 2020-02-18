import pytest

from .agent_trace_document import AgentTraceTransitionDocument, AgentTraceDocument


@pytest.fixture()
def final_trace(trace, state2):
    trace.set_final_state(state2)

    return trace


def test_agent_trace_document_created_from_trace(final_trace):
    agent_trace_document = AgentTraceDocument.from_agent_trace("agent_id", final_trace)

    assert agent_trace_document.length == 2


def test_agent_trace_transition_document_created_from_trace(final_trace):
    agent_trace_transition_document = AgentTraceTransitionDocument.from_transition(
        agent_trace_id="agent_trace_id",
        transition_index=1,
        transition_dict=final_trace[1],
    )

    assert agent_trace_transition_document.action == "DOWN"
