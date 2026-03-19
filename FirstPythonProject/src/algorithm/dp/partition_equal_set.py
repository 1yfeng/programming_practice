from typing import List
class PartitionEqualSet:
    def can_partiton(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        sorted_list = sorted(nums)
        n = len(nums)
        sum = [0] * 2
        for i in range(n - 1, -1, -1):
            if sum[0] <= sum[1]:
                sum[0] +=  sorted_list[i]
            else: 
                sum[1] +=  sorted_list[i]
        return sum[0] == sum[1]
    

    def can_partition_v2(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num

        if sum % 2 == 1:
            return False
        m = sum // 2
        dp = [[False] * (m + 1) for _ in range(n)]
        dp[0][0] = True
        if nums[0] <= m:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(m + 1):
                if nums[i] <= j:
                    dp[i][j] |= dp[i - 1][j - nums[i]]
                dp[i][j] |= dp[i - 1][j]

        return dp[n -1][m]