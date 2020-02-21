import React from 'react';
import Link from 'next/link';
import Button from '@material-ui/core/Button';

const headerStyle = {
  width: "100%",
  height: 60,
  margin: 10,
};

const Header: React.FC = () => (
  <div style={headerStyle}>
    <Link href="/">
      <a>
        <Button variant="outlined">Home</Button>
      </a>
    </Link>
  </div>
);

export default Header;
