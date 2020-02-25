import React from "react";
import { useRouter } from 'next/router';
import CircularProgress from '@material-ui/core/CircularProgress';

import Layout from '../../../../components/Layout';
import TransitionContainer from "../../../../components/TransitionContainer";


const AgentTraceTransitionsContent = () => {
  const router = useRouter();
  const agentId = router.query.agentId;
  const traceId = router.query.traceId;

  if (agentId && traceId) {
    return <TransitionContainer agentId={agentId as string} traceId={traceId as string}/>;
  } else {
    return <CircularProgress />;
  }
};

const AgentTraceTransitions = () => (
  <Layout>
    <AgentTraceTransitionsContent />
  </Layout>
);

export default AgentTraceTransitions;
