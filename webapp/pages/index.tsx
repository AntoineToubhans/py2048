import useSWR from 'swr';

import { NextPage } from 'next';

import { Agent } from '../types/agent';
import AgentLink from "../components/AgentLink";
import Layout from '../components/Layout';


const fetcher = (url: string) => (
  fetch(url).then(r => r.json())
);

const Agents: NextPage<{}> = () => {
  const { data, error } = useSWR('/api/agents', fetcher);

  if (!data) {
    return <Layout>Loading ...</Layout>
  }
  if (error) {
    return <Layout>Error</Layout>
  }

  const agents = data.agents || [];

  return (
    <Layout>
      <h1>Agents</h1>
      <ul>
        {agents.map((agent: Agent) => (
          <li key={agent.id}>
            <AgentLink agent={agent}/>
          </li>
        ))}
      </ul>
    </Layout>
  );
};

export default Agents;
