class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        ans = []
        for i in range(n - 2):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] == -sorted_nums[i]:
                    ans.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
                elif sorted_nums[l] + sorted_nums[r] > -sorted_nums[i]:
                    r -= 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
        
        return ans

                


        