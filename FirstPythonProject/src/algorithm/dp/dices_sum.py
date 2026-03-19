class DicesSum:
    def dices_sum(self, n: int) -> list[list[int]] :
        if n < 0:
            return[]
        
        size = 6 * n
        dp = [[0.0] * (size + 1) for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1 / 6
        
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for k in range(1, 7):
                    if j - k >= (i - 1) and j - k <= 6 * (i - 1):
                        dp[i][j] += dp[i - 1][j - k] / 6
        
        result = []
        for i in range(n, size + 1):
            result.append([i, dp[n][i]])
        return result
    
    def dices_sum_fix(self, n: int) -> list[list[int]] :
        if n < 0:
            return[]
        m = 6 * n
        dp = [[0] * (m + 1) for _ in range(2)]
        for i in range(1, 6 + 1):
            dp[1][i] = 1 / 6
        new = 1
        old = 0
        for i in range(2, n + 1):
            new =  1 - new
            old =  1 - old
            for j in range(i, 6 * i + 1):
                dp[new][j] = 0
                for k in range(1, 6 + 1):    
                    if i-1 <= j - k and j - k <= (i - 1) * 6:
                        dp[new][j] = dp[new][j] + dp[old][j - k] / 6
                    
        result = []
        for i in range(n, m + 1):
            result.append([i, dp[n % 2][i]])
        return result
        #return [[i, dp[n % 2][i]] for i in range(n, m + 1)]
    

