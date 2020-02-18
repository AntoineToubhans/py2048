from elasticsearch_dsl import (
    Document,
    Keyword,
)


class AgentDocument(Document):
    name = Keyword()
    commit_sha = Keyword()

    class Index:
        name = "agents"
