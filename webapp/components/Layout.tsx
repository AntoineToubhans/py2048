import React from 'react';

import Header from './Header';

interface AuxProps  { 
  children: React.ReactNode
}

const Layout: React.FC<AuxProps> = props => (
  <div>
    <Header/>
    {props.children}
     <style jsx global>{`
        body {
          margin: 0;
          padding: 0;
          background-color: #faf8ef;
      `}</style>
  </div>
);

export default Layout;
