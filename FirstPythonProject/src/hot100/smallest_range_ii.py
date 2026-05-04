"""
LeetCode 910. Smallest Range II

给你一个整数数组 nums 和一个整数 k。
对于每个下标 i (0 <= i < nums.length)，将 nums[i] 变成 nums[i] + k 或 nums[i] - k。
nums 的分数是 nums 中最大元素和最小元素的差值。
在更改每个下标对应的值之后，返回 nums 的最小分数。

思路：
1. 先对数组排序。
2. 排序后，最优策略一定是：选择一个分割点 i，
   nums[0..i] 全部 +k，nums[i+1..n-1] 全部 -k。
   （因为如果一个较小的数 -k，而一个较大的数 +k，差值只会变大，不会更小。）
3. 枚举分割点 i (0 <= i <= n-2)：
   - 此时数组中可能的最大值 = max(nums[i] + k, nums[-1] - k)
   - 此时数组中可能的最小值 = min(nums[0] + k, nums[i+1] - k)
   - 用 (max - min) 更新答案。
4. 不分割（全部 +k 或全部 -k）的情况下，差值就是 nums[-1] - nums[0]，
   作为初始答案。

时间复杂度：O(n log n)
空间复杂度：O(1)（不计排序额外空间）
"""

from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]  # 全 +k 或全 -k 的情况

        for i in range(n - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, high - low)

        return ans


if __name__ == "__main__":
    sol = Solution()
    # 示例 1: nums=[1], k=0 -> 0
    print(sol.smallestRangeII([1], 0))
    # 示例 2: nums=[0,10], k=2 -> 6  (0+2=2, 10-2=8 -> 8-2=6)
    print(sol.smallestRangeII([0, 10], 2))
    # 示例 3: nums=[1,3,6], k=3 -> 3 (1+3=4, 3+3=6, 6-3=3 -> max=6,min=3 差=3)
    print(sol.smallestRangeII([1, 3, 6], 3))
