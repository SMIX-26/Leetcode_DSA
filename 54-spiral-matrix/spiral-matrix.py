class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rowstart = 0
        rowend = len(matrix) - 1

        colstart = 0
        colend = len(matrix[0]) - 1

        ans = []

        while rowstart <= rowend and colstart <= colend:

            # top row
            for j in range(colstart, colend + 1):
                ans.append(matrix[rowstart][j])
            rowstart += 1

            # right column
            for i in range(rowstart, rowend + 1):
                ans.append(matrix[i][colend])
            colend -= 1

            # bottom row
            if rowstart <= rowend:
                for j in range(colend, colstart - 1, -1):
                    ans.append(matrix[rowend][j])
                rowend -= 1

            # left column
            if colstart <= colend:
                for i in range(rowend, rowstart - 1, -1):
                    ans.append(matrix[i][colstart])
                colstart += 1

        return ans



            
