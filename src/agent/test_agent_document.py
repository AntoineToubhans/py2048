from .agent_document import AgentDocument


def test_agent_document():
    agent_document = AgentDocument(name="TotoAgent", commit_sha="123456",)

    assert agent_document.name == "TotoAgent"
    assert agent_document.commit_sha == "123456"
