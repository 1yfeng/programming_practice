from typing import List
import sys
class JumpGameII:
    def jump(self, a: List[int]) -> int:
        if not a:
            return 0
        
        n = len(a)
        dp = [sys.maxsize] * n
        dp[0] = 0

        for i in range(1, min(a[0] + 1, n)):
            dp[i] = 1
        
        for i in range(1, n):
            for j in range(1, min(a[i] + 1, n)):
                if (i + j) < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n-1]
