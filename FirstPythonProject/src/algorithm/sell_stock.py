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






















    def max_profit_with_cooldown(self, prices: List[int]) -> int:
        """
        计算有冷却期的股票交易最大利润。
        
        使用动态规划，维护三种状态：
        - hold: 持有股票的最大利润
        - cooldown: 刚卖出股票（处于冷却期）的最大利润
        - rest: 不持有股票且已过冷却期的最大利润
        
        状态转移：
        - hold = max(前一个hold, 前一个rest - 当前价格)  # 保持持有或新买入
        - cooldown = hold + 当前价格  # 从持有卖出
        - rest = max(前一个rest, 前一个cooldown)  # 保持rest或从cooldown转入
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if not prices or len(prices) < 2:
            return 0
        
        hold = -prices[0]  # 第一天买入
        cooldown = 0       # 第一天的冷却期状态（未进行任何交易）
        rest = 0           # 第一天的rest状态（未进行任何交易）
        
        for i in range(1, len(prices)):
            # 保存前一个状态
            prev_hold = hold
            prev_cooldown = cooldown
            prev_rest = rest
            
            # 当前可以持有：保持持有或从rest状态买入
            hold = max(prev_hold, prev_rest - prices[i])
            
            # 当前冷却期：从持有状态卖出
            cooldown = prev_hold + prices[i]
            
            # 当前rest状态：保持rest或从cooldown转入
            rest = max(prev_rest, prev_cooldown)
        
        # 最终最大利润是cooldown或rest中的最大值（不能持有股票）
        return max(cooldown, rest)

    



