class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        result = s[0]
        n = len(s)

        def extend(s: str, i: int) -> str:
            n = len(s)
            result_1 = s[i]
            result_0 =  ""
            for j in range(min(i + 1, n - 1 - (i + 1) + 1)):
                if s[i - j] != s[i + 1 + j]:
                    break
                result_0 = s[i - j] + result_0 + s[i - j]

            for j in range(1, min(i + 1,  n - 1 - (i + 1) + 2)):
                if s[i - j] != s[i + j]:
                    break
                result_1 = s[i - j] + result_1 + s[i - j] 

            if len(result_0) > len(result_1 ):
                return result_0
            return result_1

        for i in range(n):
            r = extend(s, i)
            print(f"i = {i}, {r}")
            if len(result) < len(r):
                result = r
        return result