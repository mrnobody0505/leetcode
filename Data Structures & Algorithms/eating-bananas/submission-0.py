class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal_hour(k):
            return sum([math.ceil(pile / k) for pile in piles])
        
        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            mid = l + ((r - l) // 2)
            if cal_hour(mid) <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
            

        