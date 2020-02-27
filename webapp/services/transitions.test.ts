import nock from 'nock';
import { getTransition } from "./transitions";


describe("getTransition()", () => {
  beforeAll(() => {
    nock('http://localhost:9200')
      .post('/agent_trace_transitions/')
      .query(true)
      .reply(200, {});
  });

  it("should return one transition", async () => {
    expect(await getTransition("pv4wV3ABBiPUjHVugvFI", 42)).toEqual({
      id: "Pf4wV3ABBiPUjHVumvfO",
      agent_trace_id: "pv4wV3ABBiPUjHVugvFI",
      transition_index: 42,
      state_before_action: {
        c0_0: 2,
        c0_1: 4,
        c0_2: 16,
        c0_3: 2,
        c1_0: 4,
        c1_1: 64,
        c1_2: 64,
        c1_3: 8,
        c2_0: 8,
        c2_1: 8,
        c2_2: 8,
        c2_3: 0,
        c3_0: 4,
        c3_1: 0,
        c3_2: 2,
        c3_3: 0,
      },
      action: "RIGHT",
      reward: 144,
      action_compute_time: 0.0000019073486328125,
      state_after_action: {
        c0_0: 2,
        c0_1: 4,
        c0_2: 16,
        c0_3: 2,
        c1_0: 0,
        c1_1: 4,
        c1_2: 128,
        c1_3: 8,
        c2_0: 0,
        c2_1: 0,
        c2_2: 8,
        c2_3: 16,
        c3_0: 2,
        c3_1: 0,
        c3_2: 4,
        c3_3: 2,
      },
    });
  });
});
