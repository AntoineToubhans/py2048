import React from "react";
import { useRouter } from 'next/router';
import CircularProgress from '@material-ui/core/CircularProgress';

import withLayout from '../../../../components/Layout';
import TransitionContainer from "../../../../components/TransitionContainer";

const AgentTraceTransitions = () => {
  const router = useRouter();
  const traceId = router.query.traceId;

  if (traceId) {
    return <TransitionContainer url={`/api/traces/${traceId}`}/>;
  } else {
    return <CircularProgress />;
  }
};

export default withLayout(AgentTraceTransitions);
