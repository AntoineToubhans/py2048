import React from "react";
import useSWR from 'swr';
import { Subtract } from 'utility-types';

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

const withData = <T extends WrappedComponentProps>(
  WrappedComponent: React.ComponentType<T>
): React.FC<
    Subtract<T, WrappedComponentProps> & WrapperComponentProps
  > => ({url, ...otherProps}) => {
    const {data, error} = useSWR(url, fetcher);

    if (!data) {
      return (
        <div style={{textAlign: "center", margin: 10}}>
          <CircularProgress/>
        </div>
      );
    }
    if (error) {
      return (
        <>
          <ErrorIcon/> An error occurred.
        </>
      );
    }

    // Hack to trick typescript
    const unknownOtherProps: unknown = otherProps;

    return (
      <WrappedComponent
        {...unknownOtherProps as T}
        data={data}
      />
    );
  };

export default withData;
