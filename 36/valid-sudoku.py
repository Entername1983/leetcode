# Sudoku board, 9*9


## check rows
## check columns, board[i][j]
## check grids:
#### grids will be the trickier parts
#### grid 1 row 0 - 2, col 0 - 2
#### grid 2 row 0 - 2, col 3 - 5
#### grid 3 row 0 - 2, col 6 - 8


### brute force --> many loops
### only filled cells are validated

## loop through eahc item in the grid.  If not . --> loop through each item in the same row
                                                 ## --> loop through each item in the same column
                                                 ## --> loop throughh each item in the same grid


## make 27 different boxes
from collections import defaultdict
from typing import DefaultDict, Set


def isValidSudoku(board: list[list[str]]) -> bool:
    cols: DefaultDict[int, Set[int]] = defaultdict(set)
    rows: DefaultDict[int, Set[int]] = defaultdict(set)
    grids: DefaultDict[str, Set[int]] = defaultdict(set)
    

    
    
    n: int = len(board)
    for r in range(n):
        for c in range(n):
            cell_v = board[r][c]
            if cell_v != ".":
                if int(cell_v) in cols[c]:
                    return False
                if int(cell_v) in rows[r]:
                    return False
                row_i: int = r // 3
                col_i: int = c // 3
                grid_key: str = str(row_i) + str(col_i)
                if int(cell_v) in grids[grid_key]:
                    return False
                cols[c].add(int(cell_v))
                rows[r].add(int(cell_v))
                grids[grid_key].add(int(cell_v))
    return True
                
print(isValidSudoku(board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))