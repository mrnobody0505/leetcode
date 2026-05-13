class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        mem = {}
        def dfs(a):
            if a == 0:
                return 0
            if a < 0:
                return float('inf')
            if a in mem:
                return mem[a]
            ans = float('inf')
            for coin in coins:
                ans = min(ans, 1 + dfs(a - coin))
            mem[a] = ans
            return ans
        
        temp = dfs(amount)
        if temp == float('inf'):
            return -1
        return temp

        