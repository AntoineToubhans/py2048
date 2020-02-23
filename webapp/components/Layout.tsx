import React from 'react';
import Head from "next/head";

import Header from './Header';

interface AuxProps  { 
  children: React.ReactNode
}

const Layout: React.FC<AuxProps> = props => (
  <>
    <Head>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css?family=Roboto:300,400,500"
      />
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/icon?family=Material+Icons"
      />
    </Head>
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
  </>
);

export default Layout;
