from elasticsearch_dsl import (
    Document,
    Integer,
    Float,
    InnerDoc,
    Keyword,
    Object,
)

from src.game import Action


class AgentTraceActionRatioInnerDoc(InnerDoc):
    UP = Float()
    DOWN = Float()
    LEFT = Float()
    RIGHT = Float()


class AgentTraceDocument(Document):
    agent_id = Keyword()
    length = Integer()
    max_tile = Integer()
    score = Integer()
    mean_compute_action_time = Float()
    action_ratio = Object(AgentTraceActionRatioInnerDoc)

    class Index:
        name = "agent_traces"

    @staticmethod
    def from_agent_trace(agent_id, agent_trace):
        """ Create a document from an agent trace

        Args:
            agent_id (str): the agent ID in ES.
            agent_trace (src.agent.agent_trace.AgentTrace): an agent trace

        Returns:
            AgentTraceDocument: the document that can be saved in es.
        """
        return AgentTraceDocument(agent_id=agent_id, **agent_trace.describe())


class StateInnerDoc(InnerDoc):
    c0_0 = Integer()
    c0_1 = Integer()
    c0_2 = Integer()
    c0_3 = Integer()
    c1_0 = Integer()
    c1_1 = Integer()
    c1_2 = Integer()
    c1_3 = Integer()
    c2_0 = Integer()
    c2_1 = Integer()
    c2_2 = Integer()
    c2_3 = Integer()
    c3_0 = Integer()
    c3_1 = Integer()
    c3_2 = Integer()
    c3_3 = Integer()

    @staticmethod
    def from_state(state):
        length_x, length_y = state.shape

        return StateInnerDoc(
            **{
                f"c{index_x}_{index_y}": state[index_x, index_y]
                for index_x in range(length_x)
                for index_y in range(length_y)
            }
        )


class AgentTraceTransitionActionProbabilitiesInnerDoc(InnerDoc):
    UP = Float()
    DOWN = Float()
    LEFT = Float()
    RIGHT = Float()


class AgentTraceTransitionDocument(Document):
    agent_trace_id = Keyword()
    transition_index = Integer()
    state_before_action = Object(StateInnerDoc)
    action = Keyword()
    action_probabilities = Object(AgentTraceTransitionActionProbabilitiesInnerDoc)
    reward = Integer()
    action_compute_time = Float()
    state_after_action = Object(StateInnerDoc)

    class Index:
        name = "agent_trace_transitions"

    @staticmethod
    def from_transition(agent_trace_id, transition_index, transition_dict):
        """ Create a document from an agent trace

        Args:
            agent_trace_id (str): the agent trace ID in ES.
            transition_index (int): the index of the transition in the trace
            transition_dict (dict): a dictionary representing a transition e.g., a trace element trace[0]

        Returns:
            AgentTraceTransitionDocument: the document that can be saved in es.
        """
        action_probabilities = {
            action.name: transition_dict["action_probabilities"].get(action, 0)
            for action in Action
        }

        return AgentTraceTransitionDocument(
            agent_trace_id=agent_trace_id,
            transition_index=transition_index,
            state_before_action=StateInnerDoc.from_state(
                transition_dict["state_before_action"]
            ),
            action=transition_dict["action"].name,
            action_probabilities=action_probabilities,
            reward=transition_dict["reward"],
            action_compute_time=transition_dict["action_compute_time"],
            state_after_action=StateInnerDoc.from_state(
                transition_dict["state_after_action"]
            ),
        )
