# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if n < 1:
            return False
        row = -1
        for i in range(m):
            if target >= matrix[i][0]:
                row = i
        if row > -1:
            return target in matrix[row]
        else:
            return False 

matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
    ]
ans = Solution().searchMatrix(matrix, 16)
print(ans)
