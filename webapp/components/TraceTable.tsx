import React from "react";
import MaterialTable from "material-table";
import { useRouter } from 'next/router'
import LinearProgress from '@material-ui/core/LinearProgress';


const formatPercentage = (value: number): string => `${(100 * value).toFixed(2)} %`;

interface TraceTableProps {
  agentId: string;
}

enum ColumnTitle {
  Id = 'ID',
  Score = 'Score',
  MaxTile = 'Max Tile',
  Length = '# Steps',
  MeanComputeTime = 'Mean compute time (ms)',
  LeftActionRatio = 'Left moves',
  UpActionRatio = 'Up moves',
  RightActionRatio = 'Right moves',
  DownActionRatio = 'Down moves',
}

const SORT_FIELD_BY_COLUMNS: { [key in ColumnTitle]: string } = {
  [ColumnTitle.Id]: 'id',
  [ColumnTitle.Score]: 'score',
  [ColumnTitle.MaxTile]: 'max_tile',
  [ColumnTitle.Length]: 'length',
  [ColumnTitle.MeanComputeTime]: 'mean_compute_action_time',
  [ColumnTitle.LeftActionRatio]: 'action_ratio.LEFT',
  [ColumnTitle.UpActionRatio]: 'action_ratio.UP',
  [ColumnTitle.RightActionRatio]: 'action_ratio.RIGHT',
  [ColumnTitle.DownActionRatio]: 'action_ratio.DOWN',
};


const TraceTable: React.FC<TraceTableProps> = ({ agentId}) => {
  const router = useRouter();

  return (
    <MaterialTable
      title={`Traces for agent "${agentId}"`}
      actions={[
        {
          icon: 'visibility',
          tooltip: 'See trace',
          onClick: (event, rowData) => {
            // Awful hack as rowData is either a row or an array of rows.
            const traceId = (rowData as {id: string}).id;
            return router.push(`/agents/${agentId}/traces/${traceId}`);
          },
        },
      ]}
      columns={[
        {
          title: ColumnTitle.Id,
          field: 'id',
        },
        {
          title: ColumnTitle.Score,
          field: 'score',
        },
        {
          title: ColumnTitle.MaxTile,
          field: 'max_tile',
          render: rowData => (
            <>
              <div>{rowData.max_tile}</div>
              <LinearProgress variant="determinate" value={100 * Math.log2(rowData.max_tile) / 15}/>
            </>
          ),
        },
        {
          title: ColumnTitle.Length,
          field: 'length',
        },
        {
          title: ColumnTitle.MeanComputeTime,
          field: 'mean_compute_action_time',
          render: rawData => (rawData.mean_compute_action_time * 1000).toFixed(6),
        },
        {
          title: ColumnTitle.LeftActionRatio,
          field: 'action_ratio',
          render: rawData => formatPercentage(rawData.action_ratio.LEFT),
        },
        {
          title: ColumnTitle.UpActionRatio,
          field: 'action_ratio',
          render: rawData => formatPercentage(rawData.action_ratio.UP),
        },
        {
          title: ColumnTitle.RightActionRatio,
          field: 'action_ratio',
          render: rawData => formatPercentage(rawData.action_ratio.RIGHT),
        },
        {
          title: ColumnTitle.DownActionRatio,
          field: 'action_ratio',
          render: rawData => formatPercentage(rawData.action_ratio.DOWN),
        },
      ]}
      data={async query => {
        const url = `/api/agents/${agentId}/traces`;

        const data = {
          page: query.page,
          pageSize: query.pageSize,
          sort: query.orderBy ? `${SORT_FIELD_BY_COLUMNS[query.orderBy.title as ColumnTitle]}:${query.orderDirection}` : undefined,
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
      options={{
        pageSize: 10,
        actionsColumnIndex: -1,
      }}
    />
  );
};

export default TraceTable;
