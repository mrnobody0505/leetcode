class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Find max(min(heights[i], heights[j]) * |i - j|)
        l = 0
        r = len(heights) - 1
        ans = - 1
        while l < r:
            ans = max(ans, min(heights[l], heights[r]) * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return ans
