from typing import List
class ProfitableSchemes:

    # before ac try again after watch video
    def profitable_schemes(self, g: int, p: int, group: List[int], profit: List[int]) -> int:
        if not group or not profit:
            if p > 0:
                return 0
            else:
                return 1
            
        n = len(group)
        dp = [[[0] * (p + 1) for _ in range(g + 1)] for _ in range(n + 1)]

        dp[0][0][0] = 1
        # dp[0][0][1] = 0    inti 0 default
        for i in range(1, n + 1):
            for j in range(g + 1):
                for k in range(p + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if 0 <= (j - group[i - 1]):
                        if 0 <= (k - profit[i - 1]): 
                            dp[i][j][k] += dp[i - 1][j - group[i - 1]][k - profit[i - 1]]
                        else:
                            #(k - profit[i - 1] 小于 0 说明我需要的profit没了 此时 request profit 是负数 负数没有记录 用0足够 因为确实存在大于p的利润
                            #没有贴切 那就用最大可用的
                            dp[i][j][k] += dp[i - 1][j - group[i - 1]][0]
        
        result = 0
        for i in range(g + 1):
            result += dp[n][i][p]
        return result
    
    
    def profitable_schemes_rolling_array(self, g: int, p: int, group: List[int], profit: List[int]) -> int:
        if not group or not profit:
            if p > 0:
                return 0
            else:
                return 1
            
        n = len(group)
        dp = [[[0] * (p + 1) for _ in range(g + 1)] for _ in range(2)]

        new = 0
        old = 1 - new 
        dp[new][0][0] = 1
        # dp[0][0][1] = 0    inti 0 default
        for i in range(1, n + 1):
            new = 1 - new
            old = 1 - old
            for j in range(g + 1):
                for k in range(p + 1):
                    dp[new][j][k] = dp[old][j][k]
                    if 0 <= (j - group[i - 1]):
                        if 0 <= (k - profit[i - 1]): 
                            dp[new][j][k] += dp[old][j - group[i - 1]][k - profit[i - 1]]
                        else:
                            #(k - profit[i - 1] 小于 0 说明我需要的profit没了 此时 request profit 是负数 负数没有记录 用0足够 因为确实存在大于p的利润
                            #没有准确 那就用最大可用的 因为题目中都是大于0 的利润 
                            dp[new][j][k] += dp[old][j - group[i - 1]][0]
        
        result = 0
        for i in range(g + 1):
            result += dp[new][i][p]
        return result
    

    """ 
    profitable_schemes_my 的问题
Bug：在同一轮迭代中，dp 被原地修改，导致后续读取到的是已被污染的值，造成重复计数。

这是经典的 0/1 背包错误。当处理第 i 个 crime 时，遍历 visited 中的 pair 并更新 dp，但后面的 pair 读取 dp 时，已经包含了本轮前面 pair 写入的新值。

反例
g=10, p=2, group=[1,1,1], profit=[1,1,1]，正确答案是 4（{0,1}, {0,2}, {1,2}, {0,1,2}），但此方法返回 6。

具体原因：处理 item 2 时，先处理 pair (1,1)，将 dp[2][2] 从 1 更新为 3；接着处理 pair (2,2) 时读到的 dp[2][2] 已经是 3（应该是旧值 1），导致 dp[3][2] 被多加。
    """
    def profitable_schemes_my(self, g: int, p: int, group: List[int], profit: List[int]) -> int:
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
  
            
