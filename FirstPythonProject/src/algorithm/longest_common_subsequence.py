class LongestCommonSubsequence:
    def longest_common_subsequence(self, a: str, b: str):
        if not a or not b:
            return 0
        
        n = len(a)
        m = len(b)
        dp = [[0] * m for _ in range(n)]
        if a[0] == b[0]:
            dp[0][0] = 1

        for i in range(1, m):
            if dp[0][i - 1] == 1 or a[0] == b[i]:
                dp[0][i] = 1

        for i in range(1, n):
            if dp[i - 1][0] == 1 or a[i] == b[0]:
                dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if a[i] == b[j]:
                    dp[i][j] = dp[i - 1][i - 1]  + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[n-1][m-1]