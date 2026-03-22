from typing import List
class ProfitableSchmea:
    def profitable_schema(self, g: int, p: int, group: List[int], profit: List[int]) -> int:
        if not group:
            if p > 0:
                return 0
            else: 
                return 1
            
        n = len(group)
        dp = [[0] * (p + 1) for _ in range(g+1)]
        
        visited  = set([])
        for i in range(n):
            new_visited = set([]) 
            for pair in visited:
                if ((pair[0] + group[i]) <= g):
                    if pair[1] + profit[i] > p:
                        dp[pair[0] + group[i]][p] += dp[pair[0]][pair[1]]
                        new_visited.add((pair[0] + group[i], p))
                    else:
                        dp[pair[0] + group[i]][pair[1] + profit[i]] += dp[pair[0]][pair[1]]
                        new_visited.add((pair[0] + group[i], pair[1] + profit[i]))    
            visited.update(new_visited)
            if (group[i] <= g):
                if profit[i] > p:
                    dp[group[i]][p] += 1
                    visited.add((group[i], p))
                else:
                    dp[group[i]][profit[i]] += 1
                    visited.add((group[i], profit[i]))
        
        total_sum = 0
        for i  in range(g +1):
            total_sum += dp[i][p]
        return total_sum