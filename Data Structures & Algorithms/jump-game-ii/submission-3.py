class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        curr_end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = max_reach
        
        return jumps

        