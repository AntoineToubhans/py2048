import React from "react";
import { useRouter } from 'next/router';

import Layout from '../../../../components/Layout';
import Transition from "../../../../components/Transition";


const AgentTraceTransitionsContent = () => {
  const router = useRouter();
  const agentId = router.query.agentId;
  const traceId = router.query.traceId;

  if (agentId && traceId) {
    return <Transition agentId={agentId as string} traceId={traceId as string}/>;
  } else {
    return <div>"Loading"</div>;
  }
};

const AgentTraceTransitions = () => (
  <Layout>
    <AgentTraceTransitionsContent />
  </Layout>
);

export default AgentTraceTransitions;
