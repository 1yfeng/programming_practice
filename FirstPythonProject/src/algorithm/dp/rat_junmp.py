from typing import List
class RatJump:
    def rat_jump(self, n: int, stricked: List[bool]) -> int:
        if n == 0 or not stricked:
            if stricked and stricked[0] == True:
                   return 0
            return 1
        mod_constant = 1000000000 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        if stricked[n]:
            dp[n][0] = 0
        else:
            dp[n][0] = 1

        for i in range(n - 1, -1, -1):
            if stricked[i]:
                continue

            for j in range(n - i, min((n - i) // 4 - 1, 0), -1):
                if j % 2 ==1 :
                    if  i + 1 <= n:
                        dp[i][j] += dp[i + 1][j - 1]
                    if  i + 2 <= n:
                        dp[i][j] += dp[i + 2][j - 1]
                    if  i + 4 <= n:
                        dp[i][j] += dp[i + 4][j - 1]
                else:
                    if  i + 1 <= n:
                        dp[i][j] += dp[i + 1][j - 1]
                    if  i + 3 <= n:
                        dp[i][j] += dp[i + 3][j - 1]
                    if  i + 4 <= n:
                        dp[i][j] += dp[i + 4][j - 1]
                dp[i][j] = dp[i][j] % mod_constant
            print(f"i={i}, dp[i] = {dp[i]}")
        
        result = 0
        for i in range(n + 1):
            result =  (result + dp[0][i]) % mod_constant
        return result
    
if __name__ == "__main__":
    rat = RatJump()
    # print(rat.rat_jump(3, [False, False, False, False]))
    print(rat.rat_jump(4, [False, False, True, False, False]))

                
            
         
