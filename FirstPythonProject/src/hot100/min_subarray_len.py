class Solution:
    def minSubArrayLen_v1(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        
        prefix_sum = [0]
        stack = [0]
        result = sys.maxsize
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + nums[i])
            if stack and prefix_sum[-1] - stack[0]:
                m = len(stack)
                for j in range(m -1, -1, -1):
                    if (prefix_sum[-1] - prefix_sum[stack[j]] >= target):
                        result = min(result, (i + 1 - stack[j]))
                        break
            
            while prefix_sum[stack[-1]] >= prefix_sum[-1]:
                stack.pop()
            stack.append(i + 1)
        if result == sys.maxsize:
            return 0
        return result 
         
        
        