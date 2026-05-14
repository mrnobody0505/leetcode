class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            heapq.heappush(heap, (-(x * x + y * y), i))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [points[i] for _, i in list(heap)]
        