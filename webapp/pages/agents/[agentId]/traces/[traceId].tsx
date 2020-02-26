import React from "react";
import { useRouter } from 'next/router';
import CircularProgress from '@material-ui/core/CircularProgress';

import withLayout from '../../../../components/Layout';
import TransitionContainer from "../../../../components/TransitionContainer";


const AgentTraceTransitions = () => {
  const router = useRouter();
  const agentId = router.query.agentId;
  const traceId = router.query.traceId;

  if (agentId && traceId) {
    return <TransitionContainer agentId={agentId as string} traceId={traceId as string}/>;
  } else {
    return <CircularProgress />;
  }
};

export default withLayout(AgentTraceTransitions);
