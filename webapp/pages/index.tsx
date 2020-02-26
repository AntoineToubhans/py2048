import React from "react";
import useSWR from 'swr';
import { NextPage } from 'next';

import { Agent } from '../types/agent';
import withLayout from '../components/Layout';
import AgentTable from "../components/AgentTable";


const fetcher = (url: string) => (
  fetch(url).then(r => r.json())
);

const Agents: NextPage<{}> = () => {
  const { data, error } = useSWR('/api/agents', fetcher);

  if (!data) {
    return <>Loading ...</>
  }
  if (error) {
    return <>Error</>
  }

  const agents: Agent[] = data.agents || [];

  return (
    <>
      <h1>Agents</h1>
      <AgentTable agents={agents}/>
    </>
  );
};

export default withLayout(Agents);
