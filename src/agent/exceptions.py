class AgentTraceFinalStateAlreadySetError(Exception):
    """
        Error raised when the final state has been set and
            somebody is trying to add more data to the trace.
    """


class AgentTraceFinalStateNotSetError(Exception):
    """
        Error raised when the final state has NOT been set and
            somebody is trying to access data.
    """
