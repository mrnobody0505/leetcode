class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        if n < m:
            return False
        hm = {}
        for i in range(m):
            hm[s1[i]] = hm.get(s1[i], 0) + 1
            hm[s2[i]] = hm.get(s2[i], 0) - 1
        
        if all(v == 0 for v in hm.values()): 
            return True
        
        for i in range(m, n):
            hm[s2[i]] = hm.get(s2[i], 0) - 1
            hm[s2[i - m]] = hm.get(s2[i - m], 0) + 1
            if all(v == 0 for v in hm.values()):
                return True
        
        return False


        