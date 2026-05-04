"""
LeetCode 31. 下一个排列

原地修改，O(n) 时间，O(1) 空间。

核心思路（推荐解 / 经典解均基于同一算法，无本质区别）：
  1. 从右向左找第一个"升序对"的左端点 i，即 nums[i] < nums[i+1]
     —— i 左侧已是字典序最大的后缀，无法再大，必须在 i 处"进位"
  2. 从右向左找第一个大于 nums[i] 的位置 j，交换 nums[i] 与 nums[j]
     —— 使第 i 位尽量小地变大
  3. 翻转 i+1 之后的后缀（此时后缀必为降序），使其变为最小的升序排列
  若第 1 步找不到 i（整个数组降序），说明已是最大排列，直接翻转整个数组
"""

from typing import List


# 推荐解：标准双指针实现，语义清晰
def next_permutation(nums: List[int]) -> None:
    n = len(nums)

    # 步骤 1：从右向左找第一个下降点 i（nums[i] < nums[i+1]）
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # 步骤 2：从右向左找第一个大于 nums[i] 的元素 j，交换
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # 步骤 3：翻转 i+1 之后的后缀
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# 经典解：用切片赋值翻转后缀，写法更 Pythonic
def next_permutation_pythonic(nums: List[int]) -> None:
    n = len(nums)

    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # 切片反转后缀（原地赋值，仍为 O(1) 额外空间）
    nums[i + 1:] = nums[i + 1:][::-1]
