from typing import List
import sys
import heapq

class ShortestSubarray:

    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1;

        records = []
        sum = 0
        n = len(nums)
        result = n + 1
        for i in range(n):
            if nums[i] >= k:
                return 1;
        
            if records and (sum + nums[i]) <= 0:
                records.clear()
                sum = 0
            else :
                records.append(i)
                sum += nums[i]

            if sum >= k:
                left_try = list(records)
                left_sum = sum
                while (left_sum - nums[left_try[0]]) >= k:
                    left_sum -=  nums[left_try[0]]
                    left_try.pop(0)
                left_result = left_try[-1] - left_try[0]  + 1

                right_sum = sum
                right_try = list(records)
                while (right_sum - nums[right_try[-1]]) >= k:
                    right_sum -=  nums[right_try[-1]]
                    right_try.pop()
                right_result = right_try[-1] - right_try[0]  + 1
                
                if left_result < right_result :
                    if left_result < result:
                        result = left_result
                        sum = left_sum
                        records = left_try
                else:
                    if right_result < result:
                        result = right_result
                        sum = right_sum
                        records = right_try


                if records and result > (records[-1] - records[0] + 1):
                    result = records[-1] - records[0] + 1
        if result == (n + 1):
            return -1
        return result
                
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0;
        
        n = len(nums)
        records = [0 for _  in range(n)]

        if nums[n -1] >= k:
            return 1;
       
        for step in range(n):
            for start in range(n - step):
                records[start] = records[start] + nums[start + step]
                if records[start] >= k:
                    return step + 1
        
        return -1
    
    def shortest_subarray_equal(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        prefix_sum = self.__get_prefix_sum(nums)
        result = 0
        sum2indexs = {0:[0]}
        for end in range(len(nums)):
            if (prefix_sum[end + 1] - k) in sum2indexs:
                for i in range(len(sum2indexs[prefix_sum[end + 1] - k])):
                    result += 1

            if prefix_sum[end + 1] in sum2indexs:
                sum2indexs[prefix_sum[end + 1]].append(end)
            else:
                sum2indexs[prefix_sum[end + 1]] = [end]
        
        return result


    #greater_equal
    def shortest_subarray_ge(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        
        result = sys.maxsize
        prefix_sum = self.__get_prefix_sum(nums)

        start = 0
        end = len(nums)
        record = -1
        while start <= end:
            mid = start + (end - start) // 2
            if self.is_vaild(prefix_sum, k, mid):
                record = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return record
    
    def is_vaild(self, prefix_sum, k, length) -> bool:
        if length <= 0:
            return False
        heap = HeapLazyDeletionPair()
        for end in range(len(prefix_sum) - 1):
            heap.delete(end - length)

            heap.push(prefix_sum[end], end)
            if prefix_sum[end + 1] - k >= heap.top()[0]:
                return True
        return False

    def __get_prefix_sum(self, nums: list[int]) -> list[int]:
        if not nums:
            return None
        
        prefix_sum = [0] 
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[i] + nums[i])
        return prefix_sum
        

class HeapLazyDeletionPair:
    def __init__(self, data = None):
        if data == None:
              data = []
        self.delete_set = set()
        self.heap = data          
      
    def heapify(self):
        heapq.heapify(self.heap)

    def push(self, val, index):
        heapq.heappush(self.heap, (val, index))

    def delete(self, id: int):
        self.delete_set.add(id)

    def _lazy_delete(self):
        while self.heap and self.heap[0][1] in self.delete_set:
            val, index = heapq.heappop(self.heap)
            self.delete_set.remove(index)
    
    def top(self):
        self._lazy_delete()
        return self.heap[0]

    def pop(self):
        self._lazy_delete()
        return heapq.heappop(self.heap)