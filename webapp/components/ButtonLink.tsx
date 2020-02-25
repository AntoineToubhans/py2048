import React from 'react';
import Link from 'next/link';
import Button from '@material-ui/core/Button';
import ButtonGroup from "@material-ui/core/ButtonGroup";

import { colors } from '../stylesheet';


interface ButtonLinkProps {
  text: string;
  href: string;
}

const ButtonLink: React.FC<ButtonLinkProps> = ({text, href}) => (
  <Button
    variant="contained"
    style={{
      backgroundColor: colors.darker,
      fontWeight: "bold",
      marginRight: 6,
    }}
  >
    <Link href={href}>
      <a style={{color: colors.white, textDecoration: "None"}}>{text}</a>
    </Link>
  </Button>
);

export default ButtonLink;
