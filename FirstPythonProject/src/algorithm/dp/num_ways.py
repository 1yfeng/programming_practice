class NumWays:
    
    def num_ways(self, steps: int, arr_len: int) -> int:
        if steps <= 0 or arr_len <= 1:
            return 1
        MOD = 10**9 + 7
        # 最远只能走到 steps//2，缩减列数
        max_pos = min(arr_len, steps // 2 + 1)
        dp = [[0] * max_pos for _ in range(2)]

        dp[1][0] = 1
        dp[1][1] = 1
        new = 1
        old = 0

        for i in range(1, steps):
            new = 1 - new
            old = 1 - old
            dp[new] = [0] * max_pos
            for j in range(max_pos):
                dp[new][j] = dp[old][j]
                if j - 1 >= 0:
                    dp[new][j] += dp[old][j - 1]
                if j + 1 < max_pos:
                    dp[new][j] += dp[old][j + 1]
                dp[new][j] %= MOD

        return dp[new][0] % MOD