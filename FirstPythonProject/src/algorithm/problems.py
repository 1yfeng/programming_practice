from typing import List
import array

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if temperatures:
            records = [0];
            results = [0] * len(temperatures);
            for i in range(1, len(temperatures)):
                if temperatures[records[-1]] >= temperatures[i]:
                    records.append(i);
                else:
                    while records and temperatures[records[-1]] < temperatures[i]:
                        index = records.pop();
                        results[index] = i - index;
                records.append(i);
            return results;     
        else:   
            return [];

    def trap(self, height: List[int]) -> int:
        if height:
            result = 0
            records = [0]
            for i in range(1, len(height)):
                if height[records[0]] <= height[i]:
                    while records:
                        result += (height[records[0]] - height[records.pop()])
                records.append(i)
            if records:
                target_height = height[records.pop()]
                for i in range(1, len(records)):
                    if height[records[-1]] >= target_height:
                        target_height = height[records.pop()]
                    else:
                        result += (target_height - height[records.pop()])
            return result
            
        else:
            return 0
        
    def largest_rectangle_area(self, heights: list[int]) -> int:
        result = 0
        if heights:
            records = [0]
            for i in range(1, len(heights)):
                if heights[i] > heights[records[-1]]:
                    records.append(i)
                elif heights[i] == heights[records[-1]]:
                    continue
                else:
                    n = len(records)
                    while records and (heights[i] < heights[records[-1]]):
                        pop_element, result = self.pop_record_calculate(records, heights, i, result)
                    records.append(i)
            
            while records:
                op_element, result = self.pop_record_calculate(records, heights, n - 1, result)
        return result
    def pop_record_calculate(self, records: list[int], heights: list[int], curIndex: int, result: int):
        n = len(records)
        for i in range(n):
            area = heights[records[n - 1 - i]] * (curIndex - records[n - 1 - i] + 1)
            if result < area:
                result = area
        pop_element = records.pop()
        return pop_element, result

    def largest_rectangle_area2(self, heights: List[int]) -> int:
        result = 0
        if not heights:
         return result
        
        n = len(heights)
        left_records = []
        right_records = []
        left_wide = array.array('i', [0] * n)
        right_wide = array.array('i', [0] * n)

        for i in range(n):
            if len(left_records) == 0 or heights[i] > heights[left_records[-1]]:
                left_records.append(i)
                left_wide[i] = left_records[-1] - 1
            else:
                while len(left_records) > 0 and heights[i] <= heights[left_records[-1]]:
                    left_records.pop()
                
                if left_records:
                    left_wide[i] = left_records[-1]
                else:
                    left_wide[i] = -1
                left_records.append(i)

            right_index = n - 1 - i
            if len(right_records) == 0 or heights[right_index] > heights[right_records[-1]]:
                right_records.append(right_index)
                right_wide[right_index] = right_records[-1] + 1
            else:
                while len(right_records) > 0 and heights[right_index] <= heights[right_records[-1]]:
                    right_records.pop()

                if right_records:
                    right_wide[right_index] = right_records[-1]
                else:
                    right_wide[right_index] = n
                right_records.append(right_index)

        for i in range(n):
            if right_wide[i] - left_wide[i] > 1 :
                area = (right_wide[i] - left_wide[i]  - 1) * heights[i]
                if area > result:
                    result = area
        return result

    def largest_rectangle_area_opt(self, heights: List[int]) -> int:
        result = 0
        if not heights:
         return result
        
        n = len(heights)
        records = []
        left_wide = array.array('i', [0] * n)
        #note: right init is n 
        right_wide = array.array('i', [n] * n)

        for i in range(n):
            while len(records) > 0 and heights[i] <= heights[records[-1]]:
                index = records.pop()
                right_wide[index] = i 

            left_wide[i] = records[-1] if records else -1 
            records.append(i)

        for i in range(n):
            if right_wide[i] - left_wide[i] > 1 :
                area = (right_wide[i] - left_wide[i]  - 1) * heights[i]
                if area > result:
                    result = area
        return result

                    