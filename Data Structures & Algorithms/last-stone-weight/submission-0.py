class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            top1 = -heapq.heappop(heap)
            top2 = -heapq.heappop(heap)
            if top1 == top2:
                continue
            new_weight = abs(top1 - top2)
            heapq.heappush(heap, -new_weight)
        
        if len(heap) == 0:
            return 0
        return -heap[0]
        
        