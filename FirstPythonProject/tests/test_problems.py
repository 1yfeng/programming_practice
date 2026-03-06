import pytest
from src.algorithm.problems import Solution

def test_dailyTemperatures_function():
    solution = Solution()
    input = [64, 40, 49, 73, 72, 35, 68, 83, 35, 73, 84, 88, 96, 43, 74, 63, 41, 95, 48, 46, 89, 72, 34, 85, 72, 59, 87, 49, 30, 32, 47, 34, 74, 58, 31, 75, 73, 88, 64, 92, 83, 64, 100, 99, 81, 41, 48, 83, 96, 92, 82, 32, 35, 68, 68, 92];
    for index,value  in enumerate(input):
        print(f"Index: {index}, Value: {value}")
    print("----->")
    result = solution.dailyTemperatures(input)
    
    for index,value  in enumerate(result):
        print(f"Index: {index}, Value: {value}")

def test_trap_function():
    solution = Solution()
    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(input)
    print(f"Trapped water: {result}")

def test_largest_rectangle_area_function():
    solution = Solution()
    input = [2,1,5,6,2,3]
    result = solution.largest_rectangle_area(input)
    print(f"Largest rectangle area: {result}")

def test_largest_rectangle_area2_function():
    solution = Solution()
    input = [2,4]
    result = solution.largest_rectangle_area2(input)
    print(f"Largest rectangle area: {result}")

def test_largest_rectangle_area_opt_function():
    solution = Solution()
    input = [5,5,1,7,1,1,5,2,7,6]
    result = solution.largest_rectangle_area_opt(input)
    print(f"Largest rectangle area: {result}")    