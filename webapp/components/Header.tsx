import React from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';

import { colors } from '../stylesheet';
import ButtonLink from "./ButtonLink";


const headerStyle = {
  width: "100%",
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
