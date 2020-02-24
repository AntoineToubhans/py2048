import React from "react";
import { useRouter } from 'next/router';

import Layout from '../../../components/Layout';
import TraceTable from "../../../components/TraceTable";


const AgentTracesContent = () => {
  const router = useRouter();
  const agentId = router.query.agentId;

  if (agentId) {
    return <TraceTable agentId={agentId as string} />;
  } else {
    return <div>"Loading"</div>;
  }
};

const AgentTraces = () => (
  <Layout>
    <AgentTracesContent />
  </Layout>
);

export default AgentTraces;
