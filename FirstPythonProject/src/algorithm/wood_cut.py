from typing import List
import sys

class WoodCut:
    def cut(self, woods: List[int], k : int) -> int:
        if not woods:
            return 0
        
        n = len(woods)
        times = k // n
        remainer = k % n

        sorted_woods = sorted(woods)
        smaller_wood = sys.maxsize
        larger_wood = sys.maxsize
        if times > 0 :
            smaller_wood = smaller_wood // times
        if  remainer > 0:
            larger_wood = sorted_woods[n-remainer] // (times + 1)

        return min(smaller_wood, larger_wood)

    def cut_binary(self, woods: List[int], k : int) -> int:
        if not woods:
            return 0
        
        n = len(woods)
        sum = 0
        max_len = 0
        for i in range(n):
            sum += woods[i]
            if max_len < woods[i]:
                max_len = woods[i]
        
        if sum < k:
            return 0
        
        left = 1
        right = max_len
        max_size = 0

        while left <= right:
            mid = left + (right - left) // 2
            if self.__is_vaild(woods, k, mid):
                max_size = mid
                start = mid + 1
            else:
                end = mid - 1

        return max_size

    def __is_vaild(self, woods: List[int], k: int, length: int) -> bool:
        count = 0
        for wood in woods:
            count += wood // length
        
        if count >= k:
            return True
        return False