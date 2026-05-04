"""
最长严格递增子序列 (Longest Increasing Subsequence, LIS)

给定整数数组 nums，返回其中最长严格递增子序列的长度。
"""

from bisect import bisect_left
from typing import List


class LongestIncreasingSubsequence:
    # ---------------------------------------------------------------
    # 推荐解法：贪心 + 二分查找    时间 O(n log n)，空间 O(n)
    # ---------------------------------------------------------------
    #
    # 核心思想：
    #   维护一个数组 tails，tails[i] 表示「长度为 i+1 的递增子序列」
    #   所能拥有的最小末尾元素。tails 始终保持严格递增。
    #
    # 对每个 num：
    #   - 在 tails 中用二分查找找到第一个 >= num 的位置 idx
    #     （bisect_left 保证「严格」递增；若是非严格递增改成 bisect_right）
    #   - 若 idx == len(tails)，说明 num 比所有末尾都大，追加，长度 +1
    #   - 否则用 num 替换 tails[idx]，让该长度的子序列末尾更小，
    #     为后续元素留出更多扩展空间
    #
    # 注意：tails 本身不一定是真实存在的某个 LIS，但其长度就是 LIS 的长度。
    # ---------------------------------------------------------------
    def length_of_LIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tails: List[int] = []
        for num in nums:
            idx = bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)

    # ---------------------------------------------------------------
    # 经典解法：动态规划         时间 O(n^2)，空间 O(n)
    # ---------------------------------------------------------------
    #
    # 状态定义：
    #   dp[i] 表示以 nums[i] 结尾的最长严格递增子序列的长度。
    #
    # 状态转移：
    #   dp[i] = max(dp[j] + 1)   其中 0 <= j < i 且 nums[j] < nums[i]
    #   若不存在这样的 j，则 dp[i] = 1（自身构成长度为 1 的序列）
    #
    # 最终答案：
    #   max(dp)
    # ---------------------------------------------------------------
    def length_of_LIS_dp(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == "__main__":
    solver = LongestIncreasingSubsequence()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("二分解法:", solver.length_of_LIS(nums))      # 4  -> [2,3,7,101]
    print("DP 解法 :", solver.length_of_LIS_dp(nums))   # 4
