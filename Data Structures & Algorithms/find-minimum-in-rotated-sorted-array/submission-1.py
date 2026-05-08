class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = 0
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                ans = nums[mid]
                r = mid - 1
        
        return ans





        