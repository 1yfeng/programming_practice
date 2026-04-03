from typing import List
class Permute:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        path = []
        visited =set([])
        result = []
        self.dfs(nums, path, visited, result)
        return result

    def dfs(self, nums: list[int], path: list[int], visited: set[int], result: list[list[int]]):
        n = len(nums)
        if len(path) == n:
            result.append(list(path))
            return 

        for i in range(n):
            if not nums[i] in visited:
                
                path.append(nums[i])
                visited.add(nums[i])
                self.dfs(nums, path, visited, result)
                path.pop()
                visited.remove(nums[i])
    
