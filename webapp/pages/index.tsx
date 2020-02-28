import React from "react";
import { NextPage } from 'next';

import withLayout from '../components/Layout';
import AgentTable from "../components/AgentTable";


const Agents: NextPage<{}> = () => (
  <>
    <h1>Agents</h1>
    <AgentTable url={"/api/agents"}/>
  </>
);

export default withLayout(Agents);
