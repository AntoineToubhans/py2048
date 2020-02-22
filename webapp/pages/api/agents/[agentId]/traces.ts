import { getTraces } from '../../../../services/traces';


export default async (req, res) => {
  const {
      query: { agentId },
      body: { page, pageSize },
    } = req;

  const { traces, totalCount } = await getTraces(agentId, pageSize, page);

  res.status(200).json({
    traces,
    meta: {
      totalCount,
      page,
      pageSize,
    },
  });
};
