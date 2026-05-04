class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp_l = [0] * n
        dp_r = [0] * n
        if s[0] == '(':
            dp_l[0] = 1
        result = 0
        for i in range(1, n):
            if s[i] == '(':
                dp_l[i] = dp_l[i - 1] + 1
                dp_r[i] = dp_r[i - 1]
            elif s[i] == ')':
                dp_r[i] = dp_r[i - 1] + 1
                dp_l[i] = dp_l[i - 1]
            if dp_r[i] > dp_l[i]:
                dp_r[i] = dp_l[i]
            print(f"{dp_l[i]},{dp_r[i]}")
            result = max(min(dp_l[i], dp_r[i])*2, result)
        return result