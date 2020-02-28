export interface Trace {
  id: string;
  agent_id: string;
  length: number;
  max_tile: number;
  score: number;
  mean_compute_action_time: number;
  action_ratio: {
    UP: number;
    DOWN: number;
    LEFT: number;
    RIGHT: number;
  };
}
