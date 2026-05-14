class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = []
        sub.append(nums[0])
        for i in range(1, n):
            num = nums[i]
            if num > sub[-1]:
                sub.append(num)
            else:
                l, r = 0, len(sub) - 1
                temp = 0
                while l <= r:
                    mid = l + ((r - l) // 2)
                    if sub[mid] >= num:
                        temp = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                sub[temp] = num
                # sub[i] -> smallest tail of any LIS with length i + 1
                # if num <= sub[-1], then BS to find temp st sub[temp - 1] < num < sub[temp], hence in this case
                # a LIS of length temp + 1 is formed with smaller tail (num < sub[temp]) by combining LIS of sub[temp - 1] with num
        
        return len(sub)


        