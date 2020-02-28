import React from 'react';
import Grid from '@material-ui/core/Grid';

import { Trace } from "../types/trace";
import GameKPIContainer from "./GameKPIContainer";
import {formatComputeTime, formatPercentage} from "../services/formatHelpers";

interface TraceCardProps {
  trace: Trace;
}

const TraceCard: React.FC<TraceCardProps> = ({trace}) => (
  <Grid
    container
    spacing={2}
    justify="center"
    style={{marginBottom: 15}}
  >
    <Grid item>
      <GameKPIContainer title={"Final score"} value={trace.score}/>
    </Grid>
    <Grid item>
      <GameKPIContainer title={"Max tile"} value={trace.max_tile}/>
    </Grid>
    <Grid item>
      <GameKPIContainer title={"# steps"} value={trace.length}/>
    </Grid>
    <Grid item>
      <GameKPIContainer title={"Mean Compute t.."} value={formatComputeTime(trace.mean_compute_action_time)}/>
    </Grid>
    <Grid item>
      <GameKPIContainer title={"Left action ratio"} value={formatPercentage(trace.action_ratio.LEFT)}/>
      <GameKPIContainer title={"Up action ratio"} value={formatPercentage(trace.action_ratio.UP)}/>
    </Grid>
    <Grid item>
      <GameKPIContainer title={"Right action ratio"} value={formatPercentage(trace.action_ratio.RIGHT)}/>
      <GameKPIContainer title={"Down action ratio"} value={formatPercentage(trace.action_ratio.DOWN)}/>
    </Grid>
  </Grid>
);

export default TraceCard;
