// P   A   H   N
// A P L S I I G
// Y   I   R
//"PAHNAPLSIIGYIR"
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
// place elements in a grid of heigh numRows
// read grid line by line
// or calculate how many lines to columns to skip
function convert(s, numRows) {
    var grid = Array.from({ length: numRows }, function () { return []; });
    var changeRow = 0;
    var changeCol = 0;
    var row = 0;
    var col = 0;
    if (numRows === 1) {
        return s;
    }
    for (var _i = 0, s_1 = s; _i < s_1.length; _i++) {
        var char = s_1[_i];
        console.log("row", row);
        console.log("col", col);
        console.log("char", char);
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
    var finalList = [];
    for (var i = 0; i < numRows; i++) {
        var rowList = grid[i].join("");
        finalList = __spreadArray(__spreadArray([], finalList, true), [rowList], false);
    }
    return finalList.join("");
}
// console.log(convert("PAYE", 3));
console.log(convert("AB", 1));
// console.log(convert("PAYPALISHIRING", 4));
