import sys

class Trap:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        left_height = height[0]
        right_height = height[right]
        result = 0
        while left <= right:
            while left <= right and left_height <= right_height:
                left += 1
                if height[left] > left_height:
                    left_height = height[left]
                else:
                    result = min(left_height, right_height) - height[left]
            
            while left <= right and left_height >= right_height:
                right += 1
                if height[right] > right_height:
                    right_height = height[right]
                else:
                    result = min(left_height, right_height) - height[right]
        
        return result 
    

    def trap_v1(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_barrier = [0] * n 
        right_barrier = [0] * n

        left_max = -sys.maxsize - 1
        right_max = -sys.maxsize - 1
        for i  in range(n):
            if left_max  < height[i]:
                left_max =  height[i]
            left_barrier[i] = left_max

            if right_max < height[n - 1 -i]:
                right_max =  height[n - 1 -i]
            right_barrier[n - 1 -i] = right_max

        result = 0
        for i in range(n):
            if min(left_barrier[i], right_barrier[i]) > height[i]:
                result += min(left_barrier[i], right_barrier[i]) - height[i]
        return result


