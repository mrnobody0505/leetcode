class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        max_reach = 0

        for i in range(n):
            if i > max_reach:
                break
            new_reach = i + nums[i]
            if new_reach > max_reach:
                for k in range(max_reach + 1, min(new_reach + 1, n)):
                    dp[k] = min(dp[k], dp[i] + 1)
                max_reach = min(new_reach, n - 1)

        return dp[n - 1]