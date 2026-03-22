class distinct_subseq_ii:
    def distinct_subseq_ii(self, s: str):
        if not s:
            return 1
        mod_constant = 1000000000+7
        n = len(s)
        dp = [0] * n
        dp[0]=1
        has_letters = set([s[0]])
        for i in range(1, n):
            if s[i] not in has_letters:
                dp[i] = 1
                has_letters.add(s[i])
            for j in range(i - 1, -1, -1):
                dp[i] += dp[j]
                if s[j] == s[i]:
                    break
                
            dp[i] = dp[i] %mod_constant
        result = 0
        for i in range(n):
            result += dp[i]
        return result % mod_constant
