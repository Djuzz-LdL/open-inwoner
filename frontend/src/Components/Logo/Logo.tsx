import React from 'react';
import {Link} from 'react-router-dom';
import './Logo.scss';

interface LogoProps {
  alt?: string,
  src?: string,
}

export function Logo(props: LogoProps) {
  return (
    <Link className="logo" to="/">
      <img className="logo__image" src={props.src} alt={props.alt}/>
    </Link>
  );
}

Logo.defaultProps = {
  alt: 'Logo van gemeente',
  src: '/src/assets/logo.svg',
}
