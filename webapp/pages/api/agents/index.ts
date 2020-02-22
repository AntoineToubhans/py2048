import { getAgents } from '../../../services/agents';


export default async (req, res) => {
  const agents = await getAgents();

  res.status(200).json({agents});
};
