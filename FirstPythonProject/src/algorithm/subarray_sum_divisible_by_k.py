from __future__ import annotations

from collections import defaultdict


class SubarraySumDivisibleByK:
    """Count non-empty subarrays whose sum is divisible by k."""

    @staticmethod
    def count_recommended(nums: list[int], k: int) -> int:
        """Recommended solution: prefix sum + modulo frequency.

        Time complexity: O(n)
        Space complexity: O(min(n, k)) for non-negative k when modulo set is bounded.
        """
        if k == 0:
            raise ValueError("k must not be 0")

        count = 0
        prefix_mod = 0
        mod_freq: dict[int, int] = defaultdict(int)
        mod_freq[0] = 1

        for num in nums:
            prefix_mod = (prefix_mod + num) % k
            count += mod_freq[prefix_mod]
            mod_freq[prefix_mod] += 1

        return count

    @staticmethod
    def count_classic(nums: list[int], k: int) -> int:
        """Classic solution: enumerate all subarrays by two loops.

        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        if k == 0:
            raise ValueError("k must not be 0")

        count = 0
        n = len(nums)

        for left in range(n):
            sub_sum = 0
            for right in range(left, n):
                sub_sum += nums[right]
                if sub_sum % k == 0:
                    count += 1

        return count


if __name__ == "__main__":
    sample_nums = [4, 5, 0, -2, -3, 1]
    sample_k = 5

    print(SubarraySumDivisibleByK.count_recommended(sample_nums, sample_k))  # 7
    print(SubarraySumDivisibleByK.count_classic(sample_nums, sample_k))      # 7
