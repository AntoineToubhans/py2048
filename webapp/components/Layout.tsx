import React from 'react';

import Header from './Header';

interface AuxProps  { 
  children: React.ReactNode
}

const layoutStyle = {
  margin: 20,
  padding: 20,
  border: '1px solid #DDD'
};

const Layout: React.FC<AuxProps> = props => (
  <div style={layoutStyle}>
    <Header />
    {props.children}
  </div>
);

export default Layout;