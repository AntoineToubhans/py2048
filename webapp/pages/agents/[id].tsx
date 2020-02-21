import { useRouter } from 'next/router';

import Layout from '../../components/Layout';


const Content = () => {
  const router = useRouter();

  return (
    <>
      <h1>Agent {router.query.id}</h1>
      <p>Placeholder for traces.</p>
    </>
  );
};

const AgentTraces = () => (
  <Layout>
    <Content />
  </Layout>
);

export default AgentTraces;
