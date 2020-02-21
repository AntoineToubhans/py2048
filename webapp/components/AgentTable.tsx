import React from "react";
import Link from 'next/link';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import { Agent } from '../types/agent';


interface AgentTableProps {
  agents: Agent[];
}

const AgentTable: React.FC<AgentTableProps> = ({ agents }) => (
  <TableContainer component={Paper}>
    <Table stickyHeader aria-label="sticky table">
      <TableHead>
        <TableRow>
          <TableCell>Agent (name)</TableCell>
          <TableCell align="right">ID</TableCell>
          <TableCell align="right">Commit</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {agents.map(agent => (
          <Link href="/agents/[id]" as={`/agents/${agent.id}`} key={agent.id}>
            <TableRow hover>
              <TableCell component="th" scope="row">
                {agent.name}
              </TableCell>
              <TableCell align="right">{agent.id}</TableCell>
              <TableCell align="right">{agent.commit_sha}</TableCell>
            </TableRow>
          </Link>
        ))}
      </TableBody>
    </Table>
  </TableContainer>
);

export default AgentTable;
