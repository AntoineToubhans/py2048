import React from 'react';
import GridCell from "./GridCell";

interface GridRowProps {
  value1: number;
  value2: number;
  value3: number;
  value4: number;
}

const GridRow: React.FC<GridRowProps> = ({value1, value2, value3, value4}) => (
  <div>
    <GridCell value={value1}/>
    <GridCell value={value2}/>
    <GridCell value={value3}/>
    <GridCell value={value4} isLastCellInRow={true}/>
  </div>
);

export default GridRow;
