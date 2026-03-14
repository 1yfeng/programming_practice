from typing import List
class FindMaximumXOR:
    def find_max_xor(self, nums:List[int]):
        if not nums:
            return 0
        n = len(nums)

        max = 0
        for i in range(n):
            if max < nums[i]:
                max = nums[i]
        print(f"max = {max}")
        index = self.get_highest_index(max)
        print(f"index = {index}")
        target = (2 ** index) - 1 - max
        print(f"target = {target}")
        sorted_list = sorted(nums)
        match_num = self.find_match(target, sorted_list)
        print(match_num)
        return match_num ^ max
        
    def get_highest_index(self, num: int) -> int:
        last_vail_index  = None

        start = 0
        end = 31
        while start <= end:
            mid = start + (end - start) // 2
            print(f"mid = {mid}")
            if num == 2 ** mid:
                return mid + 1 
            elif num < 2 ** mid:
                end = mid - 1
                last_vail_index = mid
            
            elif num > 2** mid:
                start = mid + 1
        return last_vail_index
    
    def find_match(self, num: int, sorted_list: list) -> int:
        last_vail_index  = 0
        start = 0
        end = len(sorted_list)
        while start <= end:
            mid = start + (end - start) // 2
            if num == sorted_list[mid]:
                return num
            elif num < sorted_list[mid]:
                end = mid - 1        
            elif num > sorted_list[mid]:
                start = mid + 1
                last_vail_index = mid
        if num - sorted_list[last_vail_index]  < sorted_list[last_vail_index + 1] - num:
            return sorted_list[last_vail_index]   
        else:
            return sorted_list[last_vail_index + 1]   

