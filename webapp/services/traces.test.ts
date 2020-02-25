import nock from 'nock';
import {getOneById, getTraces} from './traces';


const RAW_TRACE = {
  _index : "agent_traces",
  _type : "_doc",
  _id : "pv4wV3ABBiPUjHVugvFI",
  _score : 1.0,
  _source : {
    agent_id: "hf4wV3ABBiPUjHVuce72",
    length: 119,
    max_tile: 128,
    score: 1096,
    mean_compute_action_time: 2.54446,
    action_ratio: {
      UP: 0.31932773109243695,
      RIGHT: 0.25210084033613445,
      DOWN: 0.21008403361344538,
      LEFT: 0.2184873949579832,
    },
  },
};

describe("getTraces()", () => {
  beforeAll(() => {
    nock('http://localhost:9200')
      .post('/agent_traces/_search')
      .query(true)
      .reply(200, {
        hits: {
          total: {
            value: 42,
            relation: "eq"
          },
          max_score: 1.0,
          hits: [RAW_TRACE],
        },
      });
  });

  it("should returns traces", async () => {
    expect(await getTraces("hf4wV3ABBiPUjHVuce72", 1, 0, "score:desc")).toEqual({
      totalCount: 42,
      traces: [{
        id : "pv4wV3ABBiPUjHVugvFI",
        agent_id: "hf4wV3ABBiPUjHVuce72",
        length: 119,
        max_tile: 128,
        score: 1096,
        mean_compute_action_time: 2.54446,
        action_ratio: {
          UP: 0.31932773109243695,
          RIGHT: 0.25210084033613445,
          DOWN: 0.21008403361344538,
          LEFT: 0.2184873949579832,
        },
      }],
    });
  });
});

describe("getOneById()", () => {
  beforeAll(() => {
    nock('http://localhost:9200')
      .get('/agent_traces/_doc/pv4wV3ABBiPUjHVugvFI')
      .query(true)
      .reply(200, RAW_TRACE);
  });

  it("should returns traces", async () => {
    expect(await getOneById("pv4wV3ABBiPUjHVugvFI")).toEqual({
      id: "pv4wV3ABBiPUjHVugvFI",
      agent_id: "hf4wV3ABBiPUjHVuce72",
      length: 119,
      max_tile: 128,
      score: 1096,
      mean_compute_action_time: 2.54446,
      action_ratio: {
        UP: 0.31932773109243695,
        RIGHT: 0.25210084033613445,
        DOWN: 0.21008403361344538,
        LEFT: 0.2184873949579832,
      },
    });
  });
});
