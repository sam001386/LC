# One dimensional DP
# Attention: initial condition of DP

class Solution(object):
    def numDecodings(self, s):
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        two_dig = 0
        if int(s[0]) == 0:
            return 0
        for i in range(1, len(s)+1):
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i - 1] 
            if i > 1:
                two_dig = int(s[i-2])*10 + int(s[i-1])
                if 10 <= two_dig <= 26:
                    dp[i] += dp[i - 2]
        
        return dp[-1]
