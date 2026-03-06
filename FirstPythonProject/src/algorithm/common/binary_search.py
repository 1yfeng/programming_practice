from typing import List
import sys

class BinarySearch:
    def binary_search_equal(self, nums, k) -> int:
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid]  == k:
                return mid
            elif nums[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] == k:
            return start
        if nums[end] == k:
            return end
        
        return -1
    
    #看看如何用二分法在你最开始给出的 $0, 0, 0, 1, 1, 1$ 序列中，精准找到第一个 $1$ 出现的位置（即下标 $4$）？
    def binary_search_min(self, nums, k) -> int:
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid]  >= k:
                end = mid - 1
            else:
                start = mid + 1
        return start
    
    def fin_min(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        min = start
        while start <= end:
            mid = start + (end -  start) // 2
            if nums[mid] >= nums[min]:
                start = mid + 1
            else:
                min = mid
                end = mid - 1
        
        return nums[min]

    def fin_min(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        min = start
        while start <= end:
            mid = start + (end -  start) // 2
            if nums[mid] >= nums[0]:
                start = mid + 1
            else:
                min = mid
                end = mid - 1
        
        return nums[min]