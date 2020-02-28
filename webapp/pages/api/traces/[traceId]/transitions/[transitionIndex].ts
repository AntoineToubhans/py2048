import { getTransition } from "../../../../../services/transitions";

export default async (req, res) => {
  const { traceId, transitionIndex } = req.query;
  const parsedTransitionIndex = parseInt(transitionIndex);

  const transition = await getTransition(traceId, parsedTransitionIndex);

  res.status(200).json(transition);
};
