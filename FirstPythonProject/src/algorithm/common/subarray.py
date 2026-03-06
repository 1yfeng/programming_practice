from typing import List 
from collections import deque
import sys

class Subarray:
    def shortest_subarray_sum_eg_k(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        
        subarray_len = sys.maxsize
        prefix_sum = self.get_prefix_sum(nums)
        dq = deque()
        for i in range(len(prefix_sum)):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                subarray_len = min(subarray_len, i - dq.popleft())
   
            while dq and prefix_sum[dq[-1]]  >= prefix_sum[i]:
                dq.pop()
            
            dq.append(i)
        
        if subarray_len == sys.maxsize:
            return -1
        return subarray_len 

    
    def get_prefix_sum(self, nums: list[int]) -> list[int]:
        if not nums:
            return None
        
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        return prefix_sum
    

