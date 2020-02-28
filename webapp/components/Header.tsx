import React from 'react';
import { useRouter } from 'next/router';
import ButtonLink from "./ButtonLink";


const headerStyle = {
  height: 60,
  margin: 10,
};

const Header: React.FC = () => {
  const router = useRouter();
  const agentId = router.query.agentId;
  const traceId = router.query.traceId;

  return (
    <div style={headerStyle}>
      <ButtonLink href="/" text="Home" />
      {agentId && <ButtonLink href={`/agents/${agentId}`} text={`Agent "${agentId}"`} />}
      {traceId && <ButtonLink href={`/agents/${agentId}/traces/${traceId}`} text={`Trace "${traceId}"`} />}
    </div>
  );
};

export default Header;
