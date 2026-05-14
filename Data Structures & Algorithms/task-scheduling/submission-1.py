class Solution:
    def leastInterval(self, tasks, n):
        hm = {}
        for task in tasks:
            hm[task] = hm.get(task, 0) + 1

        ready = []   # max-heap by frequency (-freq)
        waiting = [] # min-heap by avail_time

        for task, freq in hm.items():
            heapq.heappush(ready, (-freq, task))

        t = 0
        while ready or waiting:
            t += 1
            if ready:
                neg_freq, task = heapq.heappop(ready)
                if neg_freq + 1 < 0:  # still has work left
                    heapq.heappush(waiting, (t + n, neg_freq + 1, task))
            if waiting and waiting[0][0] == t:
                _, neg_freq, task = heapq.heappop(waiting)
                heapq.heappush(ready, (neg_freq, task))

        return t