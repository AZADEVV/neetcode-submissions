class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1
        middle = (l + r) // 2

        while l <= r:
            if target == matrix[middle][0]:
                return True
            elif target < matrix[middle][0]:
                r = middle - 1
            else:
                l = middle + 1

            middle = (l + r) // 2

        l_row = 0
        r_row = len(matrix[0]) - 1

        while l_row <= r_row:
            row_middle = (l_row + r_row) // 2

            if target == matrix[middle][row_middle]:
                return True
            elif target < matrix[middle][row_middle]:
                r_row = row_middle - 1
            else:
                l_row = row_middle + 1

        return False