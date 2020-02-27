import React from "react";
import {Divider} from "@material-ui/core";

import TraceCard from "./TraceCard";
import TransitionContainer from "./TransitionContainer";
import withData from "./DataLoaderWrapper";
import { Trace } from "../types/trace";


interface TransitionsProps {
  data: Trace;
}

const Transitions: React.FC<TransitionsProps> = ({data}) => {
  const trace: Trace = data;

  return (
    <>
      <TraceCard trace={trace}/>
      <Divider />
      <TransitionContainer traceLength={data.length} url={`/api/traces/${trace.id}/transitions/1`} />
    </>
  )
};

export default withData(Transitions);
