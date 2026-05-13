class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            dp[i][i] = True
            ans += 1
            for j in range(0, i):
                dp[i][j] = True
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[j] == s[i] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans += 1
        
        return ans
                    

        