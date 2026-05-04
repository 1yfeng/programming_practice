from typing import List
import sys
class findKthLargest:
    def find_kth_largest(self, nums: List[int], k :int) -> int:
        if not nums or len(nums) < k:
            return -sys.maxsize -1
        n = len(nums)
        target = n - k
        start = 0
        end = n -1
        mid = self.partition(nums, start, end)
        while mid != target:
            if mid > target:
                mid = self.partition(nums, start, mid - 1)
            else:
                mid = self.partition(nums, mid + 1, end)
        return mid
    
    def partition(self, nums: List[int], start: int, end: int) -> int:
        pivot = nums[start]
        while start < end:
            while  start < end and nums[end] >= pivot:
                end -= 1
            if end == start:
                break
            nums[start] = nums[end]
            start += 1
            while start < end and nums[start] < pivot:
                start += 1
            
            if end == start:
                break
            nums[end] = nums[start]
            end -= 1
        
        nums[start] = pivot
        return start  

