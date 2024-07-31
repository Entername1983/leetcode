
# give a 2d matrix m * n 
# each row is sorted in non descreasing order
# first ineger of each row is greater than the last ineger of the previous row
# find the appropriate row where the answer might be
# conduct a binary search within that row
# a binary search within a binary search
# edge cases:
## [[]], [[][][]], [[0]], [[0], [0]]

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    n = len(matrix)
    if n == 0:
        return False
    m = len(matrix[0])

    if n == 1:
        if m == 1:
            if matrix[0][0] == target:
                return True
            return False
    if m == 0:
        return False
    st_row: int = 0
    ed_row: int = n - 1
    st: int = 0
    ed: int = m - 1

    while st_row <= ed_row:
        
        md_row: int = ((ed_row - st_row)//2) + st_row      
        if matrix[md_row][0] <= target <= matrix[md_row][-1]:
            while st <= ed:
                md: int = ((ed - st )//2) + st
                if matrix[md_row][md] == target:
                    return True
                if matrix[md_row][st] <= target <= matrix[md_row][md]:
                    ed = md - 1
                else:
                    st = md + 1
                if st == ed:
                    if 0 <= st <= len(matrix[0]) -1 :
                        if matrix[md_row][st] == target:
                            return True
                        else:
                            return False
                    else:
                        return False

        if matrix[st_row][0] <= target <= matrix[md_row][-1]:
            ed_row = md_row - 1
        else:
            st_row = md_row + 1
            
            
print("RESULTS")

print(searchMatrix(matrix = [[1]], target = 3), 'false')
print(searchMatrix(matrix = [[1, 1]], target = 1), 'true')
print(searchMatrix(matrix = [[1, 3]], target = 1), 'true')
print(searchMatrix(matrix = [[1],[3],[5]], target = 3), 'true')

print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3), 'true')

print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3), 'true')
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13), 'false')