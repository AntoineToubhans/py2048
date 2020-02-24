import { getTraces } from '../../../../services/traces';


export default async (req, res) => {
  const {
      query: { agentId },
      body: { page, pageSize, sort },
    } = req;

  const { traces, totalCount } = await getTraces(agentId, pageSize, page, sort);

  res.status(200).json({
    traces,
    meta: {
      totalCount,
      page,
      pageSize,
    },
  });
};
