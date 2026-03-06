from typing import List

class PrefixSum:
    def prefix_sum(self, nums: list[int]) -> list[int]:
        if not nums:
            return nums
        
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        return prefix_sum
    
    def subarray_sum_equal(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
               
        n = len(nums)
        prefix_sum = [0]
        target_dict = {0:[0]}
        result = 0
        for i in range(n):
            if nums[i] == k:
                result += 1
            # i + 1
            prefix_sum.append(prefix_sum[-1] + nums[i])
            if prefix_sum[-1] in target_dict:
                target_dict[prefix_sum[-1]].append(i + 1)
            else:
                target_dict[prefix_sum[-1]]=[i + 1]
        if n == 1:
            return result 
        for end in range(n):
            target = prefix_sum[end + 1] - k
            if target in target_dict:
                for start in target_dict[target]:
                    if end > start:
                        result += 1

        return result 
