import {
  RequestParams,
  ApiResponse,
} from '@elastic/elasticsearch'

import { client, SearchResponse } from "./esHelpers";
import {Transition} from "../types/transition";

type TraceSearchFilter = { "agent_trace_id.keyword": string };
type TransitionIndexSearchFilter = { transition_index: number };
type SearchFilter = { term: TraceSearchFilter | TransitionIndexSearchFilter };

interface SearchBody {
  query: {
    bool: {
      filter: SearchFilter[],
    }
  };
}

type TransitionSource = Omit<Transition, "id">;

const index = "agent_trace_transitions";

export const getTransition = async (traceId: string, transitionIndex: number): Promise<Transition> => {
  const searchParams: RequestParams.Search<SearchBody> = {
    index,
    body: {
      query: {
        bool: {
          filter: [
            {term: {"agent_trace_id.keyword": traceId}},
            {term: {transition_index: transitionIndex}},
          ],
        },
      },
    },
    size: 1,
  };

  const response: ApiResponse<SearchResponse<TransitionSource>> = await client.search(searchParams);

  const transitions = response.body.hits.hits.map(
    rawTrace => ({
      id: rawTrace._id,
      ...rawTrace._source,
    })
  );

  if (transitions.length == 0) throw "No transition found";
  if (transitions.length > 1) throw "Too many transitions found";

  return transitions[0];
};
