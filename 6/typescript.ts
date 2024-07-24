// P   A   H   N
// A P L S I I G
// Y   I   R
//"PAHNAPLSIIGYIR"

// place elements in a grid of heigh numRows
// read grid line by line
// or calculate how many lines to columns to skip

function convert(s: string, numRows: number): string {
  let grid = Array.from({ length: numRows }, (): string[] => []);
  let changeRow = 0;
  let changeCol = 0;
  let row: number = 0;
  let col: number = 0;
  if (numRows === 1) {
    return s;
  }
  for (let char of s) {
    grid[row][col] = char;
    if (row === numRows - 1) {
      changeRow = -1;
      changeCol = 1;
    }
    if (row === 0) {
      changeRow = +1;
      changeCol = 0;
    }
    row += changeRow;
    col += changeCol;
  }
  let finalList: string[] = [];
  for (let i = 0; i < numRows; i++) {
    const rowList = grid[i].join("");
    finalList = [...finalList, rowList];
  }
  return finalList.join("");
}

// console.log(convert("PAYE", 3));

console.log(convert("AB", 1));
// console.log(convert("PAYPALISHIRING", 4));
