# Approach 1
class Solution(object):
    def numDecodings(self, s):
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, len(s)+1):
            # 1-bit case
            if s[i-1] == "*":
                dp[i] += dp[i-1] * 9
            elif s[i-1] != "0":
                dp[i] += dp[i-1]
            dp[i] %= MOD
            # 2-bit case
            if i >= 2:
                if s[i-2] == "*" and s[i-1] == "*":
                    dp[i] += dp[i-2] * 15 
                elif s[i-2] == "*":
                    if int(s[i-1]) <= 6:
                        dp[i] += dp[i-2] * 2
                    else:
                        dp[i] += dp[i-2] 
                elif s[i-1] == "*":
                    if int(s[i-2]) == 1:
                        dp[i] += dp[i-2] * 9
                    elif int(s[i-2]) == 2:
                        dp[i] += dp[i-2] * 6
                elif 10 <= int(s[i-2:i]) <= 26:
                    dp[i] += dp[i-2]
                
            dp[i] %= MOD

        return dp[-1]

# Approach 2
# The following approach can pass all the 217/217 test cases, 
# But still TLE in Python because of constant time limitation, 
# The OJ should have a little larger data size for this question 

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
