import {
  RequestParams,
  ApiResponse,
} from '@elastic/elasticsearch'

import { Trace } from "../types/trace";
import { client, SearchResponse } from "./es_helpers";


const index = "agent_traces";

interface SearchBody {
  query: {
    constant_score: {
      filter: {
        term: { "agent_id.keyword": string },
      },
    },
  }
}

interface TraceSource {
  agent_id: string;
  length: number;
  max_tile: number;
  score: number;
  mean_compute_action_time: number;
  action_ratio: {
    UP: number;
    DOWN: number;
    LEFT: number;
    RIGHT: number;
  };
}

export const getTraces = async (
  agentId: string,
  pageSize: number,
  page: number,
): Promise<{traces: Trace[], totalCount: number}> => {
  const from = pageSize * page;
  const size = pageSize;

  const searchParams: RequestParams.Search<SearchBody> = {
    index,
    body: {
      query: {
        constant_score: {
          filter: {
            term: { "agent_id.keyword": agentId },
          },
        },
      },
    },
    sort: ['score:desc'],
    from,
    size,
  };

  const response: ApiResponse<SearchResponse<TraceSource>> = await client.search(searchParams);

  const traces = response.body.hits.hits.map(
    rawTrace => ({
      id: rawTrace._id,
      ...rawTrace._source,
    })
  );

  return { traces, totalCount: response.body.hits.total.value }
};
