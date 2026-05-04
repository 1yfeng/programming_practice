class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        letter2index = {s[0]: 0}

        max_len = 1
        for i in range(n):
            if s[i] not in letter2index:
                dp[i] = dp[i - 1]
            else:
                next_index = letter2index[s[i]] + 1
                for j in range(dp[i - 1], next_index):
                    letter2index.pop(s[j])
                dp[i]  = next_index

            print(f"dp[i] = {dp[i] }, i = {i}")
            if (i - dp[i] + 1) > max_len:
                max_len = i - dp[i] + 1
            letter2index[s[i]] = i
        return max_len



