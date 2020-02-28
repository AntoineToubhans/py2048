import nock from 'nock';
import { getAgents } from './agents';


const RAW_AGENT_BOB_V0 = {
  _id: '123456789',
  _source: {
    name: 'BobAgent',
    commit_sha: 'b5a40f3eb36d9f8a86a63f868ea2ae467bea96a3'
  },
};

const RAW_AGENT_BOB_V1 = {
  _id: '987654321',
  _source: {
    name: 'BobAgent',
    commit_sha: '85e6ed9dda14495a439fc880d8d946edca8854bd'
  },
};

const RAW_AGENT_SPONGE = {
  _id: '987651537',
  _source: {
    name: 'SpongeAgent',
    commit_sha: 'b5a40f3eb36d9f8a86a63f868ea2ae467bea96a3'
  },
};

describe("Elasticsearch proxy", () => {
  beforeAll(() => {
    nock('http://localhost:9200')
      .post('/agents/_search')
      .reply(200, {
        hits: {
          hits: [
            RAW_AGENT_BOB_V0,
            RAW_AGENT_BOB_V1,
            RAW_AGENT_SPONGE,
          ],
        }
      });
  });

  it("should returns agents", async () => {
    expect(await getAgents()).toEqual([
      {
        id: '123456789',
        name: 'BobAgent',
        commit_sha: 'b5a40f3eb36d9f8a86a63f868ea2ae467bea96a3'
      },
      {
        id: '987654321',
        name: 'BobAgent',
        commit_sha: '85e6ed9dda14495a439fc880d8d946edca8854bd',
      },
      {
        id: '987651537',
        name: 'SpongeAgent',
        commit_sha: 'b5a40f3eb36d9f8a86a63f868ea2ae467bea96a3'
      },
    ]);
  });
});
