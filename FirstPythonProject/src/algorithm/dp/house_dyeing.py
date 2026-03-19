from typing import List
class HouseColor:
    # dp[n][0] = min(dp[n -1][1]  + ,  dp[n -1][2]) +  cost[n][0]
    # dp[n][1] = min(dp[n -1][0]  + ,  dp[n -1][2]) +  cost[n][0]
    def min_cost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        for i in range(3):
            dp[0][i] = costs[0][i]
        
        for i in range(1, n):
            for c in range(3):
                dp[i][c] = min(dp[i - 1][(c + 1) % 3], dp[i - 1][(c + 2) % 3]) + costs[i][c]
        
        return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

    def min_cost_opt_storage(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        dp = [[costs[0][0], costs[0][1], costs[0][2]]  for _ in range(2)]
        
        for i in range(1, n):
            for c in range(3):
                dp[i%2][c] = min(dp[(i-1)%2][(c + 1) % 3], dp[(i-1)%2][(c + 2) % 3]) + costs[i][c]
        
        return min(dp[(n-1)%2][0], dp[(n-1)%2][1], dp[(n-1)%2][2])
    
    def min_cost_opt_storage_v2(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        dp = [[costs[0][0], costs[0][1], costs[0][2]]  for _ in range(2)]
        
        now = 0
        old = 1
        for i in range(1, n):
            now = 1 - now
            old = 1 - old
            for c in range(3):
                dp[now][c] = min(dp[old][(c + 1) % 3], dp[old][(c + 2) % 3]) + costs[i][c]
        
        return min(dp[(n-1)%2][0], dp[(n-1)%2][1], dp[(n-1)%2][2])



