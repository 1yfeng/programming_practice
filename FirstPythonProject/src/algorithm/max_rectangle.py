from typing import List
import array

class MaxRectangle:
    def largest_rectangle_area(self, heights: List[int] ) -> int:
        if not heights:
            return 0
        
        n = len(heights)
        left_border = [-1] * n
        right_border = [n] * n
        records = []
        for i in range(n):
            while records and heights[i] <= heights[records[-1]]:
                right_border[records[-1]] = i
                records.pop()
            
            left_border[i] = records[-1] if records else -1
            records.append(i)
        
        result = max((right_border[i] - left_border[i] - 1) * heights[i] for i in range(n)) 
        return result
    
    def max_rectangle(self, matrix: List[str]) -> int:
        if not matrix or not matrix[0].strip():
            return 0
        
        result = 0
        records = []
        heights = []
        row_num = len(matrix)
        n = len(matrix[0])
        left_border = [-1] * n
        right_border = [n] * n
        for row in range(row_num):
            records.clear()
            heights.clear()
            left_border[:] = [-1] * n
            right_border[:] = [n] * n
            
            #largest_rectangle_area
            for i in range(n):
                heights.append(0)
                for row_index in range(row, -1, -1):
                    if matrix[row_index][i] == '1':
                        heights[i] += 1
                    else:
                        break

                while records and heights[i] <= heights[records[-1]]:
                    right_border[records[-1]] = i
                    records.pop()
                
                left_border[i] = records[-1] if records else -1
                records.append(i)
            
            max_area = max((right_border[i] - left_border[i] - 1) * heights[i] for i in range(n)) 
            if max_area > result:
                result = max_area
        
        return result
        
