import { GameAction, GameBoard } from "./game";


export interface Transition {
  id: string;
  agent_trace_id: string;
  transition_index: number;
  state_before_action: GameBoard;
  action: GameAction;
  reward: number;
  action_compute_time: number;
  state_after_action: GameBoard;
}
