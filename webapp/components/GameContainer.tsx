import React from 'react';

import { colors } from '../stylesheet';
import { GameBoard } from "../types/game";
import GridRow from './GridRow';


interface GameContainerProps {
  board: GameBoard;
}

const GameContainer: React.FC<GameContainerProps> = ({board}) => (
  <div style={{
    margin: "0 auto",
    padding: 15,
    backgroundColor: colors.middle,
    borderRadius: 6,
    width: 470,
    height: 470,
  }}>
    <GridRow
      value1={board.c0_0}
      value2={board.c0_1}
      value3={board.c0_2}
      value4={board.c0_3}
    />
    <GridRow
      value1={board.c1_0}
      value2={board.c1_1}
      value3={board.c1_2}
      value4={board.c1_3}
    />
    <GridRow
      value1={board.c2_0}
      value2={board.c2_1}
      value3={board.c2_2}
      value4={board.c2_3}
    />
    <GridRow
      value1={board.c3_0}
      value2={board.c3_1}
      value3={board.c3_2}
      value4={board.c3_3}
    />
  </div>
);

export default GameContainer;
