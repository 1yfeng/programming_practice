from typing import List
class CanPartition:
    def can_partition(self, nums: List[int]):
        if not nums:
            return False
        
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i]
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [[False] * (target + 1) for _ in range(n)]
        if nums[0] > target:
            return False
        elif nums[0] == target:
            return True
        
        dp[0][0] = True
        dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(target + 1):
                dp[i][j] |= dp[i -1][j]
                if 0 <= (j - nums[i]):
                    dp[i][j] |= dp[i -1][j - nums[i]]

        return dp[n-1][target]

    def can_partition_rolling_array(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)
        total_sum = 0
        for i in range(n):
            total_sum += nums[i]

        if total_sum % 2 == 1:
            return False

        target = total_sum // 2
        dp = [[False] * (target + 1) for _ in range(2)]
        new = 1
        old = 0
        if nums[0] >= target:
            if nums[0] == target:
                return True
            return False
        
        dp[new][0] = True
        dp[new][nums[0]] = True

        for i in range(1, n):
            new = 1 - new
            old = 1 - old
            #bug no init
            dp[new] = [False] * (target + 1)
            for j in range(target + 1):
                dp[new][j]  |= dp[old][j]
                if 0 <= (j - nums[i]):
                    dp[new][j]  |= dp[old][j - nums[i]]
        
        return dp[new][target] 

    def can_partition_dim_1_array(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)
        total_sum = 0
        for i in range(n):
            total_sum += nums[i]

        if total_sum % 2 == 1:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        if nums[0] >= target:
            if nums[0] == target:
                return True
            return False
        
        dp[0] = True
        dp[nums[0]] = True

        for i in range(1, n):
            for j in range(target, -1, -1):
                if 0 <= (j - nums[i]):
                    dp[j]  |= dp[j - nums[i]]
        
        return dp[target] 
