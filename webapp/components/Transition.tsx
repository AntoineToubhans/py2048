import React from "react";


interface TransitionProps {
  agentId: string;
  traceId: string;
}

const Transition: React.FC<TransitionProps> = ({ agentId, traceId}) => (
  <div>
    Agent "{agentId}", Trace "{traceId}"
  </div>
);

export default Transition;
