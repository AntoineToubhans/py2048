import nock from 'nock';
import { getTransition } from "./transitions";


const RAW_TRANSITION = {
  _index: "agent_trace_transitions",
  _type: "_doc",
  _id: "Sf4wV3ABBiPUjHVuhfIR",
  _score: 0.0,
  _source: {
    agent_trace_id: "Hv4wV3ABBiPUjHVuhPJc",
    transition_index: 42,
    state_before_action: {
      c0_0: 2,
      c0_1: 8,
      c0_2: 4,
      c0_3: 2,
      c1_0: 8,
      c1_1: 4,
      c1_2: 8,
      c1_3: 4,
      c2_0: 16,
      c2_1: 2,
      c2_2: 32,
      c2_3: 2,
      c3_0: 0,
      c3_1: 0,
      c3_2: 0,
      c3_3: 2
    },
    action: "LEFT",
    reward: 0,
    action_compute_time: 1.9073486328125E-6,
    state_after_action: {
      c0_0: 2,
      c0_1: 8,
      c0_2: 4,
      c0_3: 2,
      c1_0: 8,
      c1_1: 4,
      c1_2: 8,
      c1_3: 4,
      c2_0: 16,
      c2_1: 2,
      c2_2: 32,
      c2_3: 2,
      c3_0: 2,
      c3_1: 2,
      c3_2: 0,
      c3_3: 0
    }
  }
};

describe("getTransition()", () => {
  beforeAll(() => {
    nock('http://localhost:9200')
      .post('/agent_trace_transitions/_search')
      .query({size: 1})
      .reply(200, {
        hits: {
          total: {
            value: 1,
            relation: "eq"
          },
          max_score: 0.0,
          hits: [RAW_TRANSITION],
        },
      });
  });

  it("should return one transition", async () => {
    expect(await getTransition("Hv4wV3ABBiPUjHVuhPJc", 42)).toEqual({
      id: "Sf4wV3ABBiPUjHVuhfIR",
      agent_trace_id: "Hv4wV3ABBiPUjHVuhPJc",
      transition_index: 42,
      state_before_action: {
        c0_0: 2,
        c0_1: 8,
        c0_2: 4,
        c0_3: 2,
        c1_0: 8,
        c1_1: 4,
        c1_2: 8,
        c1_3: 4,
        c2_0: 16,
        c2_1: 2,
        c2_2: 32,
        c2_3: 2,
        c3_0: 0,
        c3_1: 0,
        c3_2: 0,
        c3_3: 2
      },
      action: "LEFT",
      reward: 0,
      action_compute_time: 1.9073486328125E-6,
      state_after_action: {
        c0_0: 2,
        c0_1: 8,
        c0_2: 4,
        c0_3: 2,
        c1_0: 8,
        c1_1: 4,
        c1_2: 8,
        c1_3: 4,
        c2_0: 16,
        c2_1: 2,
        c2_2: 32,
        c2_3: 2,
        c3_0: 2,
        c3_1: 2,
        c3_2: 0,
        c3_3: 0
      }
    });
  });
});
