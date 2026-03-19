class distinct_subseq_ii:
    def distinct_subseq_ii(self, s: str):
        if not s:
            return 1
        n = len(s)
        dp = [0] * n
        dp[0]=1
        has_letters = set([s[0]])
        for i in range(1, range(n)):
            for j in range(0)