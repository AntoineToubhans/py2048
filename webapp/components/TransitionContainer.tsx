import React from "react";
import Grid from '@material-ui/core/Grid';

import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ForwardIcon from '@material-ui/icons/Forward';
import {Divider} from "@material-ui/core";

import GameContainer from "./GameContainer";
import GameKPIContainer from "./GameKPIContainer";
import TraceCard from "./TraceCard";
import withData from "./DataLoaderWrapper";
import { formatComputeTime } from "../services/formatHelpers";
import { Transition } from "../types/transition";
import { GameAction } from "../types/game";
import { Trace } from "../types/trace";


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
  data: Trace;
}

const TransitionContainer: React.FC<TransitionContainerProps> = ({data}) => {
  const transition: Transition = {
    id: "Pf4wV3ABBiPUjHVumvfO",
    agent_trace_id: "6P4wV3ABBiPUjHVumfZ4",
    transition_index: 84,
    state_before_action: {
      c0_0: 2,
      c0_1: 4,
      c0_2: 16,
      c0_3: 2,
      c1_0: 4,
      c1_1: 64,
      c1_2: 64,
      c1_3: 8,
      c2_0: 8,
      c2_1: 8,
      c2_2: 8,
      c2_3: 0,
      c3_0: 4,
      c3_1: 0,
      c3_2: 2,
      c3_3: 0,
    },
    action: "RIGHT",
    reward: 144,
    action_compute_time: 0.0000019073486328125,
    state_after_action: {
      c0_0: 2,
      c0_1: 4,
      c0_2: 16,
      c0_3: 2,
      c1_0: 0,
      c1_1: 4,
      c1_2: 128,
      c1_3: 8,
      c2_0: 0,
      c2_1: 0,
      c2_2: 8,
      c2_3: 16,
      c3_0: 2,
      c3_1: 0,
      c3_2: 4,
      c3_3: 2,
    }
  };

  return (
    <>
      <TraceCard trace={data}/>
      <Divider />
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
            value={`${transition.transition_index} / ${data.length}`}
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
    </>
  )
};

export default withData(TransitionContainer);
