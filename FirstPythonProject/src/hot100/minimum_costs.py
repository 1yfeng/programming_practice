from typing import List
import sys

class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        if not regular and not express:
            return []

        n = len(regular)
        dp = [[sys.maxsize] * 2 for _ in range(2)]
        new = 0
        old = 1
        dp[new][0] = regular[0]
        dp[new][1] = express[0] + expressCost

        result = [min(dp[0][0], dp[0][1])]
        for i in range(1, n):
            new = 1 - new
            old = 1 - old
            dp[new][0] = min(dp[old][0] + regular[i], dp[old][1] + regular[i])
            dp[new][1] = min(dp[old][1] + express[i], dp[old][0] + express[i] + expressCost)
            result.append(min(dp[new][0], dp[new][1]))
        return result