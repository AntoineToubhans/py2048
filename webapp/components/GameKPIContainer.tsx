import React from 'react';

import { colors } from '../stylesheet';

interface ScoreContainerProps {
  title: string;
  value: number | string | React.ReactNode;
}

const GameKPIContainer: React.FC<ScoreContainerProps> = ({title, value}) => (
  <div
    style={{
      padding: "10px 25px",
      height: 35,
      width: 140,
      lineHeight: "47px",
      fontWeight: "bold",
      fontSize: 25,
      margin: "0 auto 8px auto",
      textAlign: "center",
      color: colors.white,
      backgroundColor: colors.middle,
      borderRadius: 3,
    }}
  >
    <div
      style={{
        textTransform: "uppercase",
        fontSize: 13,
        lineHeight: "13px",
        textAlign: "center",
        color: colors.middleLight,
      }}
    >
      {title}
    </div>
    <div
      style={{
        position: "relative",
        top: "-6px",
      }}
    >
      {value}
    </div>
  </div>
);

export default GameKPIContainer;
