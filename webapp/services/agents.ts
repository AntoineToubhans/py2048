import {
  RequestParams,
  ApiResponse,
} from '@elastic/elasticsearch'

import { Agent } from "../types/agent";
import { client, SearchResponse } from "./es_helpers";


const index = "agents";

interface SearchBody {
  query: {
    match_all: {},
  }
}

interface AgentSource {
  name: string;
  commit_sha: string;
}

export const getAgents = async (): Promise<Agent[]> => {
  const searchParams: RequestParams.Search<SearchBody> = {
    index,
    body: {
      query: {
        match_all: {}
      }
    }
  };

  const response: ApiResponse<SearchResponse<AgentSource>> = await client.search(searchParams);

  return response.body.hits.hits.map(
    rawAgent => ({
      id: rawAgent._id,
      name: rawAgent._source.name,
      commit_sha: rawAgent._source.commit_sha,
    })
  );
};
