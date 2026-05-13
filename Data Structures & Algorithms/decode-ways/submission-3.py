class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if n == 1:
            return 1
        dp = [1] * n
        if s[0] in "3456789":
            if s[1] == '0':
                return 0
            dp[1] = 1
        if s[0] == '2':
            if s[1] in "123456":
                dp[1] = 2
            else:
                dp[1] = 1
        if s[0] == '1':
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        
        # print(dp)
        for i in range(2, n):
            if s[i] == '0':
                if s[i - 1] in '03456789':
                    return 0
                dp[i] = dp[i - 2]
            elif s[i] in '123456':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
            else:
                if s[i - 1] == '1':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        
        return dp[n - 1]