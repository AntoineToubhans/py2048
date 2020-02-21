import React from 'react';

import Header from './Header';

interface AuxProps  { 
  children: React.ReactNode
}

const Layout: React.FC<AuxProps> = props => (
  <div>
    <Header/>
    <div style={{margin: 30}}>
      {props.children}
    </div>
     <style jsx global>{`
        body {
          margin: 0;
          padding: 0;
          color: #776e65;
          background-color: #faf8ef;
          font-family: "Clear Sans", "Helvetica Neue", Arial, sans-serif;
          font-size: 18px;
      `}</style>
  </div>
);

export default Layout;
