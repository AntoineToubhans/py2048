export const formatComputeTime = (rawValueInSecond: number): string => (
  (rawValueInSecond * 1000).toFixed(6)
);

export const formatPercentage = (rawValue: number): string => (
  `${(100 * rawValue).toFixed(2)} %`
);
