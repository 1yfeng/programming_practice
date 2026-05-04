import heapq
from collections import deque, defaultdict 



def subarray_sum_recommended(nums: List[int], k: int) -> int:
    """
    推荐解：前缀和 + 哈希表
    时间复杂度 O(n)，空间复杂度 O(n)
    """
    count = 0
    prefix_sum = 0
    freq = defaultdict(int)
    freq[0] = 1  # 前缀和为0出现1次（用于处理从下标0开始的子数组）

    for x in nums:
        prefix_sum += x
        # 若存在某个历史前缀和 pre，使得 prefix_sum - pre == k，则对应子数组和为k
        count += freq[prefix_sum - k]
        freq[prefix_sum] += 1

    return count