import React from "react";
import { useRouter } from 'next/router';
import CircularProgress from '@material-ui/core/CircularProgress';
import useSWR from "swr";

import withLayout from '../../../../components/Layout';
import TransitionContainer from "../../../../components/TransitionContainer";

const fetcher = (url: string) => (
  fetch(url).then(r => r.json())
);

const AgentTraceTransitions = () => {
  const router = useRouter();
  const agentId = router.query.agentId;
  const traceId = router.query.traceId;

  if (agentId && traceId) {

    const { data, error } = useSWR(`/api/traces/${traceId}`, fetcher);

    if (!data) {
      return (
        <CircularProgress />
      );
    }

    return <TransitionContainer trace={data}/>;
  } else {
    return <CircularProgress />;
  }
};

export default withLayout(AgentTraceTransitions);
