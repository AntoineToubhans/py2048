import React from 'react';

import { colors } from '../stylesheet';
import { GameBoard } from "../types/game";


interface GameContainerProps {
  board: GameBoard;
}

const GameContainer: React.FC<GameContainerProps> = ({board}) => (
  <div style={{
    margin: "40px auto 0 auto",
    padding: 15,
    backgroundColor: colors.middle,
    borderRadius: 6,
    width: 470,
    height: 470,
  }}>
    Placeholder
  </div>
);

export default GameContainer;
