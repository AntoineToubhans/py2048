import React from "react";
import useSWR from 'swr';
import { NextPage } from 'next';

import { Agent } from '../types/agent';
import Layout from '../components/Layout';
import AgentTable from "../components/AgentTable";


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

  const agents: Agent[] = data.agents || [];

  return (
    <Layout>
      <h1>Agents</h1>
      <AgentTable agents={agents}/>
    </Layout>
  );
};

export default Agents;
