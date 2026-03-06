from typing import List
import sys

class MyShortestSubarray:
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        
        prefix_sum = self.get_prefix_sum(nums)
        result = sys.maxsize
        records = [0]
        for i in range(len(nums)):
            while records and prefix_sum[records[-1]] >= prefix_sum[i  + 1]:
                records.pop()
        
            records.append(i + 1)

            if records and len(records) > 1 and (prefix_sum[records[-1]] - prefix_sum[records[0]]) >= k:
                start = len(records) - 2 
                while start >=  0 and  (prefix_sum[records[-1]] - prefix_sum[records[start]]) < k:
                    start  -= 1

                if start >=  0 and (records[-1] - records[start]) < result:
                    result = records[-1] - records[start] 
        
        if result == sys.maxsize:
            return -1
        else:
            return result


    def shortest_subarray_binary_search(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        
        prefix_sum = self.get_prefix_sum(nums)
        result = sys.maxsize
        records = [0]
        for i in range(len(nums)):
            while records and prefix_sum[records[-1]] >= prefix_sum[i  + 1]:
                records.pop()
        
            records.append(i + 1)

            if records and len(records) > 1 and (prefix_sum[records[-1]] - prefix_sum[records[0]]) >= k:
                target = 0
                start = 0
                end = len(records) - 2 
                while start <= end:
                    mid = start + (end - start) // 2
                    if (prefix_sum[records[-1]] - prefix_sum[records[mid]]) >= k:
                        target = mid
                        start = mid + 1
                    else:
                        end  = mid - 1               

                if target >=  0 and (records[-1] - records[target]) < result:
                    result = records[-1] - records[target] 
        
        if result == sys.maxsize:
            return -1
        else:
            return result
       
    def get_prefix_sum(self, nums: List[int]) -> list[int]:
        if not nums:
            return None
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        return prefix_sum