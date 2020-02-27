import React from "react";

import Grid from '@material-ui/core/Grid';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ForwardIcon from '@material-ui/icons/Forward';

import GameContainer from "./GameContainer";
import GameKPIContainer from "./GameKPIContainer";
import withData from "./DataLoaderWrapper";
import { formatComputeTime } from "../services/formatHelpers";
import { Transition } from "../types/transition";
import { GameAction } from "../types/game";


const getActionIcon = (action: GameAction): React.ReactNode => {
  switch (action) {
    case "DOWN":
      return <ArrowDownwardIcon />;
    case "LEFT":
      return <ArrowBackIcon />;
    case "RIGHT":
      return <ArrowForwardIcon />;
    default:
      return <ArrowUpwardIcon />;
  }
};

interface TransitionContainerProps {
  traceLength: number;
  data: Transition;
}

const TransitionContainer: React.FC<TransitionContainerProps> = ({data, traceLength}) => {
  const transition: Transition = data;

  return (
    <Grid
      container
      spacing={0}
      justify="space-around"
      alignItems="center"
      style={{textAlign: "center"}}
    >
      <Grid item xs={5}>
        <h2>Before</h2>
      </Grid>
      <Grid item xs={2}>
        <ForwardIcon fontSize="large"/>
      </Grid>
      <Grid item xs={5}>
        <h2>After</h2>
      </Grid>
      <Grid item xs={5}>
        <GameContainer board={transition.state_before_action}/>
      </Grid>
      <Grid item xs={2}>
        <GameKPIContainer
          title="Transition index"
          value={`${transition.transition_index + 1} / ${traceLength}`}
        />
        <GameKPIContainer
          title="Reward"
          value={transition.reward}
        />
        <GameKPIContainer
          title="Action"
          value={getActionIcon(transition.action)}
        />
        <GameKPIContainer
          title="Compute time (ms)"
          value={formatComputeTime(transition.action_compute_time)}
        />
      </Grid>
      <Grid item xs={5}>
        <GameContainer board={transition.state_after_action}/>
      </Grid>
    </Grid>
  )
};

export default withData(TransitionContainer);
