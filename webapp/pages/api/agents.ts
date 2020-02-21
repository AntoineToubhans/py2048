import { getAgents } from '../../services/agents'; 


export default async (req, res) => {
  const agents = await getAgents();

//  await new Promise(r => setTimeout(r, 3000));

  res.status(200).json({agents});
};