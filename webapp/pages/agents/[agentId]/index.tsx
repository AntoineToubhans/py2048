import React from "react";
import { useRouter } from 'next/router';

import withLayout from '../../../components/Layout';
import TraceTable from "../../../components/TraceTable";


const AgentTraces = () => {
  const router = useRouter();
  const agentId = router.query.agentId;

  if (agentId) {
    return <TraceTable agentId={agentId as string} />;
  } else {
    return <div>"Loading"</div>;
  }
};

export default withLayout(AgentTraces);
