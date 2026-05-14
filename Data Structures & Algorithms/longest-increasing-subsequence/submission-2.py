class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            ans = max(ans, dp[i])
        
        return ans
        