from typing import List
import sys
from collections import deque

class  SellStock:
    #Not completed
    def max_profit_III(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        k = 2
        best_start = deque([0] * k, maxlen = 2)
        best_end = deque([0] * k, maxlen = 2)
        start, end = 0 , 0
        for i in range(1, len(prices), 1):
            if prices[i] < prices[start]:
                start = i
            
            if prices[i] > prices[end]:
                end = i


        return 0
    
    def max_profit_III_partition(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        max_profit = 0
        for p_index in range(n):
            max_left_profit = self.__get_profit(prices, 0, p_index)
            max_right_profit = self.__get_profit(prices, p_index, n)
            if max_profit < max_left_profit + max_right_profit:
                 max_profit = max_left_profit + max_right_profit
        
        return max_profit

    def __get_profit(self, prices: List[int], start: int, end: int) -> int:
            min = sys.maxsize
            max_profit = 0
            for i in range(start, end, 1):
                if min > prices[i]:
                    min = prices[i]
                if max_profit < prices[i] - min:
                    max_profit = prices[i] - min
            return max_profit

    



