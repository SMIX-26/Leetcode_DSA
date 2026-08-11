class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_col = set ()

        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_col.add(j)
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_col:
                    matrix[i][j]=0
