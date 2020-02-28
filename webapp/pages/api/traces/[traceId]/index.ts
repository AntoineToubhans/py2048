import { getOneById } from "../../../../services/traces";

export default async (req, res) => {
  const trace = await getOneById(req.query.traceId);

  res.status(200).json(trace);
};
