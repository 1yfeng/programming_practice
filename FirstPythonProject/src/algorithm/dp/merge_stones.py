from typing import List
import sys
class MergeStones:
    def merge_stones(self, stones: List[int], k: int):
        if not stones:
            return 0
        
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        
        prefix_sum = self.get_prefix_sum(stones)
        dp = [[[sys.maxsize] * (k + 1) for _ in range(n)] for _ in range(n)] 
        for i in range(n):
            dp[i][i][1] = 0

        for i in range(n-2, -1, -1):
            for j in range(i + 1, n):
                for l in range(2, k + 1):
                    if l > (j - i + 1):
                        break
                    for m in range(i, j):
                        dp[i][j][l] = min(dp[i][j][l], dp[i][m][l - 1] + dp[m + 1][j][1])
                dp[i][j][1] = dp[i][j][k]  + prefix_sum[j + 1] - prefix_sum[i] 

        if dp[0][n -1][1] == sys.maxsize:
            return -1
        return dp[0][n -1][1]
    
    def get_prefix_sum(self, nums: list[int]) -> list[int]:
        result = [0]
        for num in nums:
            result.append(result[-1] + num)
        return result
    
