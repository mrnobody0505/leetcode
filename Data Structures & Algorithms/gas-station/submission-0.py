class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        curr_gas = gas[0]
        for i in range(1, len(gas)):
            if cost[i - 1] > curr_gas:
                start = i
                curr_gas = gas[i]
            else:
                curr_gas -= cost[i - 1]
                curr_gas += gas[i]
        
        return start



        