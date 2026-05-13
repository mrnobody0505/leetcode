class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            for j in range(i):
                dp[i][j] = True
        ans = (0, 0)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if ans[1] - ans[0] + 1 < j - i + 1:
                        ans = (i, j)

        return s[ans[0]: ans[1] + 1]
        
        