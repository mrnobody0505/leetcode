class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}
        def dfs(s):
            if not s:
                return True
            if s in mem:
                return mem[s]
            temp = False
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    temp = dfs(s[i+1:])
                    if temp:
                        break
            mem[s] = temp
            return temp
        
        return dfs(s)

        