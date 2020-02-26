import React from "react";
import useSWR from 'swr';

import CircularProgress from '@material-ui/core/CircularProgress';
import ErrorIcon from '@material-ui/icons/Error';


interface WrappedComponentProps {
  data: any;
}

interface WrapperComponentProps {
  url: string;
}

const fetcher = (url: string) => (
  fetch(url).then(r => r.json())
);

const withData = (WrappedComponent: React.FC<WrappedComponentProps>): React.FC<WrapperComponentProps> => ({url}) => {
  const { data, error } = useSWR(url, fetcher);

  if (!data) {
    return (
      <div style={{textAlign: "center"}}>
        <CircularProgress />
      </div>
    );
  }
  if (error) {
    return (
      <>
        <ErrorIcon /> An error occurred.
      </>
    );
  }

  return (
    <WrappedComponent data={data} />
  );
};

export default withData;
