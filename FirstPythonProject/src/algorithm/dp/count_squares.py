from typing import List
class CountSquares:
    def count_squares(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        edge_len = min(n , m)
        dp = [[[0] * m for _ in range(n)] for _ in range(2)]
        result = [0] * edge_len 
        new = 1
        old = 1 - new 
        candidates = set([])
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 1:
                    dp[new][row][col] = 1
                    result[0] += 1
                    candidates.add((row,col))
                
        for i in range(1, edge_len):
            new = 1 - new
            old = 1 - old 
            for row in range(n - i):
                for col in range(m - i):
                    dp[new][row][col] = 0
                    if dp[old][row][col] > 0:
                        dp[new][row][col] = (dp[old][row + 1][col] &
                                           dp[old][row][col + 1] &
                                           dp[old][row + 1][col + 1] )
                        if dp[new][row][col] > 0:
                            result[i] += dp[new][row][col]
        
        return sum(result)
    
    def count_squares_fix(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        edge_len = min(n , m)
        dp = [[[0] * m for _ in range(n)] for _ in range(2)]
        result = [0] * edge_len 
        new = 1
        old = 1 - new 
        candidates = set([])
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 1:
                    dp[new][row][col] = 1
                    result[0] += 1
                    candidates.add((row,col))
                
        for i in range(1, edge_len):
            new = 1 - new
            old = 1 - old 
            new_candidates = set([])
            for pair in candidates:
                if dp[old][pair[0]][pair[1]] > 0 and (pair[0] + i) < n and (pair[1] + i) < m:
                    dp[new][pair[0]][pair[1]] = 0
                    dp[new][pair[0]][pair[1]] = (dp[old][pair[0] + 1][pair[1]] &
                                        dp[old][pair[0]][pair[1] + 1] &
                                        dp[old][pair[0] + 1][pair[1] + 1] )
                    if dp[new][pair[0]][pair[1]] > 0:
                        result[i] += dp[new][pair[0]][pair[1]]
                        new_candidates.add(pair)
            
            candidates = new_candidates
        
        return sum(result)
    