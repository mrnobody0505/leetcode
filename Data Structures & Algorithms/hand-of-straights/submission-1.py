class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        # print(freq)
        heapq.heapify(hand)
        num_group = len(hand) // groupSize
        for i in range(num_group):
            curr = heapq.heappop(hand)
            while freq[curr] == 0:
                curr = heapq.heappop(hand)
            freq[curr] -= 1
            cnt = 0
            while cnt < groupSize - 1:
                if curr + 1 not in freq or freq[curr + 1] == 0:
                    return False
                freq[curr + 1] -= 1
                curr = curr + 1
                cnt += 1

        return True
        