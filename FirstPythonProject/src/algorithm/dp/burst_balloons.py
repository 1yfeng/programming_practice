from typing import List 
class Burst_Balloons:
    def max_coins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [[0] * (n) for _ in range(n)]

     
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(i, j + 1):

                    dp[i][j] = max(
                        dp[i][j],
                        (dp[i][k]+ dp[k + 1][j] + nums[i] * nums[k] * nums[k + 1])
                    )

        return dp[0][n - 1]


    def max_coins_fix(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        new_nums = [1] + nums + [1] 

        n = len(new_nums)
        dp = [[0] * (n) for _ in range(n)]

     
        for interval_len in range(3, n + 1):
            for left in range(0, n - interval_len + 1):
                right = left + interval_len -1
                for k in range(left + 1, right):

                    dp[left][right] = max(
                        dp[left][right],
                        (dp[left][k]+ dp[k][right] + new_nums[left] * new_nums[k] * new_nums[right])
                    )

        return dp[0][n - 1]
