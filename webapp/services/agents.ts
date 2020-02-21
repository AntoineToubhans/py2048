import {
  Client,
  RequestParams,
  ApiResponse,
} from '@elastic/elasticsearch'

import { Agent } from "../types/agent";


const client = new Client({ node: 'http://localhost:9200' });
const index = "agents";


interface SearchBody {
  query: {
    match_all: {},
  }
}

interface ShardsResponse {
  total: number;
  successful: number;
  failed: number;
  skipped: number;
}

interface Explanation {
  value: number;
  description: string;
  details: Explanation[];
}

interface SearchResponse<T> {
  took: number;
  timed_out: boolean;
  _scroll_id?: string;
  _shards: ShardsResponse;
  hits: {
    total: number;
    max_score: number;
    hits: Array<{
      _index: string;
      _type: string;
      _id: string;
      _score: number;
      _source: T;
      _version?: number;
      _explanation?: Explanation;
      fields?: any;
      highlight?: any;
      inner_hits?: any;
      matched_queries?: string[];
      sort?: string[];
    }>;
  };
  aggregations?: any;
}

interface Source {
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

  const response: ApiResponse<SearchResponse<Source>> = await client.search(searchParams);

  const agents = response.body.hits.hits.map(
    rawAgent => ({
      id: rawAgent._id,
      name: rawAgent._source.name,
      commit_sha: rawAgent._source.commit_sha,
    })
  );

  console.log('Formatted agents', agents);

  return agents;
};
