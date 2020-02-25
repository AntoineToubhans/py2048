import React, {CSSProperties} from 'react';


const backgroundColors: { [key in number | string]: string } = {
  0: "rgba(238, 228, 218, 0.35)",
  2: "#eee4da",
  4: "#ede0c8",
  8: "#f2b179",
  16: "#f59563",
  32: "#f67c5f",
  64: "#f65e3b",
  128: "#edcf72",
  256: "#edcc61",
  512: "#edc850",
  1024: "#edc53f",
  2048: "#edc22e",
  higher: "#3c3a32",
};

const getCellFontSize = (cellValue: number): number => {
  if (cellValue < 128) return 55;
  else if (cellValue < 1024) return 45;
  else return 35;
};

  const getCellCSSStyle = (cellValue: number): CSSProperties => {
  const backgroundColor = cellValue > 2048 ? backgroundColors.higher : backgroundColors[cellValue];
  const color = cellValue > 4 ? "#f9f6f2" : undefined;

  const fontSize = getCellFontSize(cellValue);

  return {
    backgroundColor,
    color,
    fontSize,
  };
};

interface GridCellProps {
  value: number;
  isLastCellInRow?: boolean,
}

const GridCell: React.FC<GridCellProps> = ({value, isLastCellInRow= false}) => (
  <div style={{
    width: 106.25,
    height: 106.25,
    lineHeight: "106.25px",
    textAlign: "center",
    fontWeight: "bold",
    marginRight: isLastCellInRow ? 0 : 15,
    marginBottom: 15,
    borderRadius: 3,
    display: "inline-block",
    float: "left",
    ...getCellCSSStyle(value),
  }}>
    {value > 0 ? value : ""}
  </div>
);

export default GridCell;
