import React from 'react';
import Link from 'next/link';

import { Agent } from '../types/agent';


interface AgentLinkProps {
  agent: Agent;
}

const AgentLink: React.FC<AgentLinkProps> = ({ agent }) => (
  <li>
    <Link href="/agents/[id]" as={`/agents/${agent.id}`}>
      <a>{agent.name} - {agent.commit_sha}</a>
    </Link>
  </li>
);

export default AgentLink;
