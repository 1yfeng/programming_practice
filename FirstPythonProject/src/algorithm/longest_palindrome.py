class LongestPalindrome:
    def longest_palindrome(self, s: str) -> str:
        if not s:
            return s
        
        n = len(s)
        dp = [1] * n

        if n == 1:
            return s
        max_index = 0
        if s[0] == s[1]:
            dp[1] = dp[0] + 1
            max_index = 1
        
        
        for i in range(2, n):
            if dp[i-1] == 1 and s[i] == s[i -1]:
                dp[i]  = max(dp[i], dp[i - 1]  + 1) 
            if 0 <= (i -1 - dp[i - 1]) and s[i -1 - dp[i - 1]] == s[i]:
                dp[i]  = max(dp[i - 1] + 2, dp[i])

            if dp[max_index] < dp[i]:
                max_index = i
        
        return s[max_index - dp[max_index] + 1 :max_index + 1]
            


    def longest_palindrome_fix(self, s: str) -> str:
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

