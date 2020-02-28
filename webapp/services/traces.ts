import {
  RequestParams,
  ApiResponse,
} from '@elastic/elasticsearch'

import { Trace } from "../types/trace";
import { client, SearchResponse } from "./esHelpers";


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

type TraceSource = Omit<Trace, "id">;

export const getTraces = async (
  agentId: string,
  pageSize: number,
  page: number,
  sort: string,
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
    sort,
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

export const getOneById = async (traceId: string): Promise<Trace> => {
  const { body } = await client.get({index, id: traceId});

  return {
    id: body._id,
    ...body._source,
  };
};
