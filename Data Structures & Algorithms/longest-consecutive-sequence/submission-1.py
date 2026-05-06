class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            temp = num
            cnt = 0
            while temp in s:
                cnt += 1
                visited.add(temp)
                temp -= 1
            temp = num + 1
            while temp in s:
                cnt += 1
                visited.add(temp)
                temp += 1
            ans = max(ans, cnt)
        
        return ans

        
        
        