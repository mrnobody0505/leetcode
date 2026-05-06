class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        return [k for k, v in sorted(hm.items(), key=lambda x: x[1], reverse=True)][:k]
        