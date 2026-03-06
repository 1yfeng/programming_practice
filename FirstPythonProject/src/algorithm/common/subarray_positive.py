from typing import List
import sys

class SubarrayPositive:
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prefix_sum = self.__get_prefix_sum(nums)
        start = 0
        subarray_len = sys.maxsize
        for end in range(len(nums)):
            while prefix_sum[end + 1] - prefix_sum[start] >= target:
                subarray_len = min(subarray_len, end - start + 1)
                start += 1

        if subarray_len == sys.maxsize:
             return 0
        return subarray_len
  
    def __get_prefix_sum(self, nums: List[int]) -> list[int]:
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        return prefix_sum
    

    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prefix_sum = self.__get_prefix_sum(nums)
        start = 0
        subarray_conunt = 0
        char2count  = {}
        n = len(nums)
        for start in range(n):
            while len(char2count) < target :
                if nums[end] in char2count:
                    char2count[nums[end]] += 1
                else:
                    char2count[nums[end]] = 1
                end += 1

            subarray_len += (1 + n - 1  - end)

            if char2count[nums[start]] > 1:
                char2count[nums[start]] -= 1
            else:
                char2count.remove(nums[start])
            start += 1


        if subarray_len == sys.maxsize:
             return 0
        return subarray_len