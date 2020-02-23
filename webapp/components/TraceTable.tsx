import React from "react";
import MaterialTable from "material-table";
import LinearProgress from '@material-ui/core/LinearProgress';
import {Agent} from "../types/agent";


const formatPercentage = (value: number): string => `${(100 * value).toFixed(2)} %`;


interface TraceTableProps {
  agentId: string;
}

const TraceTable: React.FC<TraceTableProps> = ({ agentId}) => (
  <MaterialTable
    title={`Traces for agent "${agentId}"`}
    columns={[
      {
        title: 'Score',
        field: 'score',
      },
      {
        title: 'Max Tile',
        field: 'max_tile',
        render: rowData => (
          <>
            <div>{rowData.max_tile}</div>
            <LinearProgress variant="determinate" value={100 * Math.log2(rowData.max_tile) / 15} />
          </>
        ),
      },
      {
        title: '# Steps',
        field: 'length',
      },
      {
        title: 'Mean compute time (ms)',
        field: 'mean_compute_action_time',
        render: rawData => (rawData.mean_compute_action_time * 1000).toFixed(6),
      },
      {
        title: 'Left moves',
        field: 'action_ratio',
        render: rawData => formatPercentage(rawData.action_ratio.LEFT),
      },
      {
        title: 'Up moves',
        field: 'action_ratio',
        render: rawData => formatPercentage(rawData.action_ratio.UP),
      },
      {
        title: 'Right moves',
        field: 'action_ratio',
        render: rawData => formatPercentage(rawData.action_ratio.RIGHT),
      },
      {
        title: 'Down moves',
        field: 'action_ratio',
        render: rawData => formatPercentage(rawData.action_ratio.DOWN),
      },
    ]}
    data={async query => {
      const url = `/api/agents/${agentId}/traces`;

      const data = {
        page: query.page,
        pageSize: query.pageSize,
      };

      const response = await fetch(url, {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "post",
        body: JSON.stringify(data),
      });
      const result = await response.json();

      return {
        data: result.traces,
        ...result.meta,
      };
    }}
  />
);

export default TraceTable;
