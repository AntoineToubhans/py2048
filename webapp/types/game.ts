export interface GameBoard {
  c0_0: number;
  c0_1: number;
  c0_2: number;
  c0_3: number;
  c1_0: number;
  c1_1: number;
  c1_2: number;
  c1_3: number;
  c2_0: number;
  c2_1: number;
  c2_2: number;
  c2_3: number;
  c3_0: number;
  c3_1: number;
  c3_2: number;
  c3_3: number;
}

export type GameAction = "UP" | "RIGHT" | "DOWN" | "LEFT";
