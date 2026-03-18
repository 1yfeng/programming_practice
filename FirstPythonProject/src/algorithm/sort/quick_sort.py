class QuickSort:
    def quick_sort(self, nums: list[int], start: int, end: int):
        if start >= end:
            return 
        mid = self.partion(start, end)
        self.quick_sort(nums, start, mid -1)
        self.quick_sort(nums, mid + 1, end)


    def partition(self, nums: list[int], start: int, end:int) -> int:
        pivot = nums[start]

        while start < end:
            while start < end and pivot < nums[end]:
                end -= 1
            if start != end:
                nums[start] = nums[end]
            
            while start < end and pivot >= nums[start]:
                start += 1
            if start != end:
                nums[end] = nums[start]
        nums[start] = pivot
        return start
