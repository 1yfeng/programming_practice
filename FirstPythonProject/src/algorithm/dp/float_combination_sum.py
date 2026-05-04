import math
import heapq
class FloatCombinationSum:
    def float_combination_sum(self, a: list[float], target: int):
        if not a:
            return None
        
        n = len(a)
        min_sum = 0
        costs = [0.0] * n
        for i in range(n):
            t = math.floor(a[i])
            min_sum += t
            costs[i]= a[i] - t
        
        adjust = target - min_sum

        ceil_indexs = heapq.nlargest(adjust, enumerate(costs), key=lambda p: p[1])
        pass 

    def float_combination_sum_dp(self, a: list[float], target: int):
        if not a:
            return None
        n = len(a)
        dp = [[float("inf")] * (target + 1) for _ in range(n)]
        prev = [[-1] * (target + 1) for _ in range(n)]
        a0_floor = math.floor(a[0])
        a0_ceil = math.ceil(a[0])
        dp[0][a0_floor] = a[0] - a0_floor
        prev[0][a0_floor] = 0
        dp[0][a0_ceil] = a0_ceil - a[0]
        prev[0][a0_ceil] = 1
        candidate = set([a0_floor, a0_ceil])

        for i in range(1, n):
            new_candidate = set([])
            for c in candidate:
                ai_floor = math.floor(a[i])

                if (c + ai_floor) <= target and dp[i][c + ai_floor] > (dp[i-1][c] + a[i] - ai_floor):
                    dp[i][c + ai_floor] =  (dp[i-1][c] + a[i] - ai_floor)
                    prev[i][c + ai_floor] =  0
                    new_candidate.add(c + ai_floor)

                ai_ceil = math.ceil(a[i])
                if ((c + ai_ceil) <= target and  dp[i][c + ai_ceil] > (dp[i-1][c] + ai_ceil - a[i])):
                    dp[i][c + ai_ceil] =  (dp[i-1][c] + ai_ceil - a[i])
                    prev[i][c + ai_ceil] =  1
                    new_candidate.add(c + ai_ceil)
            candidate = new_candidate

        result = [0] * n
        value = target
        for i in range(n -1, -1, -1):
            if prev[i][value] == 1:
                result[i] = int(math.ceil(a[i]))         
            else:
                result[i] = int(math.floor(a[i]))
            value -= result[i]    
        
        return result
