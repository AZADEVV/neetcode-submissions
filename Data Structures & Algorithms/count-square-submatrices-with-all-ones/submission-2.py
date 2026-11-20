class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return sum(matrix[0])
        
        count = 0
        
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
        for d in dp:
            for c in d:
                count += c

        return count