from typing import List
class CountSquares:
    def count_squares_right_down(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        up = [[0] * m for _ in range(n)]
        left = [[0] * m for _ in range(n)]
        result = 0
        for i in range(n):
            dp[i][0] = up[i][0] = left[i][0] = matrix[i][0]
            if matrix[i][0] == 1:
                result +=1
        for i in range(m):
            dp[0][i] = up[0][i] = left[0][i] = matrix[0][i]
            if matrix[0][i] == 1:
                result +=1
        if matrix[0][0] == 1:
                result -=1
       
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    continue
                up[i][j] = up[i - 1][j] + 1
                left[i][j] = left[i][j - 1] + 1
                dp[i][j] = min(up[i - 1][j], left[i][j -1], dp[i - 1][j - 1]) + 1
                result += dp[i][j]
        
        return result
    