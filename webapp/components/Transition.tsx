import React, { useCallback, useState } from "react";
import { Divider } from "@material-ui/core";

import TraceCard from "./TraceCard";
import TransitionContainer from "./TransitionContainer";
import withData from "./DataLoaderWrapper";
import { Trace } from "../types/trace";
import { useEventListener } from "../hooks";


interface TransitionsProps {
  data: Trace;
}

const Transitions: React.FC<TransitionsProps> = ({data}) => {
  const trace: Trace = data;
  const [transitionIndex, setTransitionIndex] = useState(trace.length - 1);

  const handler = useCallback(
    (event) => {
      if (event.keyCode == 39) {
        setTransitionIndex((transitionIndex + 1) % trace.length);
      } else if (event.keyCode == 37) {
        setTransitionIndex((trace.length + transitionIndex - 1) % trace.length);
      }
    },
    [transitionIndex, setTransitionIndex]);

  useEventListener('keydown', handler);

  return (
    <>
      <TraceCard trace={trace}/>
      <Divider />
      <TransitionContainer
        traceLength={data.length}
        url={`/api/traces/${trace.id}/transitions/${transitionIndex}`}
      />
    </>
  )
};

export default withData(Transitions);
