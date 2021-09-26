class Solution(object):
    def numDecodings(self, s):
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, len(s)+1):
            for j in range(1, 27):
                if 1 <= j <= 9:
                    if s[i-1] == "*" or int(s[i-1]) == j:
                        dp[i] += dp[i-1]
                elif i >= 2:
                    units = s[i-1:i]
                    tens = s[i-2:i-1]
                    if ((tens == "*" and j//10) or (tens != "*" and int(tens) == j//10)) and\
                     ((units == "*" and j%10) or (units != "*" and int(units) == j%10)):
                        dp[i] += dp[i-2]
            dp[i] %= MOD
        
        return dp[-1]
