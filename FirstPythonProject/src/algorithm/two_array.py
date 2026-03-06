from typing import List
class TwoArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums1 or not nums2:
            return 

        index1 = m - 1
        index2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if index1 > -1 and index2 > -1:
                if (nums1[index1] >= nums2[index2]):
                    nums1[i] = nums1[index1]
                    index1 -= 1
                else:
                    nums1[i] = nums2[index2]
                    index2 -= 1
            elif index1 > -1: 
                nums1[i] = nums1[index1]
                index1 -= 1
            else:
                nums1[i] = nums2[index2]
                index2 -= 1               

        return 
    
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return 0
        
        heater_index = 0
        radius = 0
        heater_size =len(heaters)
        for i in range(len(houses)):
            while  (heater_index < heater_size -1 and 
                 abs(houses[i] - heaters[heater_index]) > abs(houses[i] - heaters[heater_index + 1])):
                heater_index  += 1

            distance = abs(houses[i] - heaters[heater_index])
            if radius < distance:
                radius = distance

        return radius

    def find_radius_with_disorder(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return 0
        
        radius = 0
        heaters.sort()
        n = len(heaters)
        for i in range(len(houses)):
            # find <= houses[i]
            left = self.__binary_search(heaters, houses[i], 0, n - 1)
            if left == -1:
                distance = heaters[0] - houses[i] 
            else:
                if left < n - 1 and (houses[i] - heaters[left]) > (heaters[left + 1] - houses[i]):
                    distance = heaters[left + 1] - houses[i]
                else :
                    distance = houses[i] - heaters[left]

            if radius < distance:
                radius = distance

        return radius

    def __binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        if not nums:
            return -1
        
        record = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                record = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return record 

    def find_radius_with_disorder_non_returnning_pointer(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return 0
        
        houses_sorted = sorted(houses)
        heaters_sorted = sorted(heaters)
        print(f"houses_sorted[1521] = {houses_sorted[1521]}, houses_sorted[1522] = {houses_sorted[1522]}")
        print(f"heaters_sorted[1521] = {heaters_sorted[1521]}, heaters_sorted[1522] = {heaters_sorted[1522]}")
        n = len(houses)
        m = len(heaters)
        heaters_index = 0
        radius = 0
        for i in range(n):
            distance = abs(heaters_sorted[heaters_index] - houses_sorted[i])
            if i == 1521:
                print()
            while (heaters_index < m - 1 and 
                   abs(heaters_sorted[heaters_index] - houses_sorted[i]) >= abs(heaters_sorted[heaters_index + 1] - houses_sorted[i])):
                heaters_index += 1
                distance = abs(heaters_sorted[heaters_index] - houses_sorted[i])

            if distance > radius:
                radius = distance
        
        return radius

