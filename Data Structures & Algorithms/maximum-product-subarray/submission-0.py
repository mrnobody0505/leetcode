class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = ans = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            temp = (num, cur_max * num, cur_min * num)
            cur_min = min(temp)
            cur_max = max(temp)
            ans = max(ans, cur_max)
        
        return ans
        