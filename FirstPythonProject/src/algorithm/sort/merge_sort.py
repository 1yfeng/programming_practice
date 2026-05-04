class MergeSort:
    def merge_sor_v_1(self, nums:list[int]):
        if not nums:
            return 
        
        n = len(nums)
        right = n - 1
        left = 0
        return self.merge_sort_internal(nums, left, right)

    def merge_sort_internal(self, nums: list[int], start: int, end: int):
        if start > end:
            return []
        if start == end:
            return [nums[start]]

        mid = start + (end - start) // 2
        left_sort = self.merge_sort_internal(nums, start, mid)
        right_sort = self.merge_sort_internal(nums, mid + 1, end)

        return self.merge(left_sort, right_sort)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []

        left_i = 0
        left_len = len(left)

        right_i = 0
        right_len = len(right)

        while left_i < left_len and right_i < right_len:
            if left[left_i] <= right[right_i]:
                result.append(left[left_i]) 
                left_i +=1
            else:
                result.append(right[right_i])
                right_i +=1
        
        while left_i < left_len:
            result.append(left[left_i])
            left_i +=1

        while right_i < right_len:
            result.append(right[right_i])
            right_i +=1

        return result
    

    def merge_sort(self, nums:list[int]) -> list[int]:
        size = len(nums)
        if size <= 1:
            return nums
        mid = size // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

    def merge_v2(self, left: list[int], right: list[int]) -> list[int]:
        result = []

        left_i = 0
        left_len = len(left)

        right_i = 0
        right_len = len(right)

        while left_i < left_len and right_i < right_len:
            if left[left_i] <= right[right_i]:
                result.append(left[left_i]) 
                left_i +=1
            else:
                result.append(right[right_i])
                right_i +=1
        
        result.extend(left[left_i:])
        # while left_i < left_len:
        #     result.append(left[left_i])
        #     left_i +=1

        result.extend(right[right_i:])
        # while right_i < right_len:
        #     result.append(right[right_i])
        #     right_i +=1

        return result
    



if __name__ == "__main__":
    sort = MergeSort()
    print(sort.merge_sort([9, 2,5 ,7, 1]))