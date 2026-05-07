class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm = {}
        for c in t:
            hm[c] = hm.get(c, 0) + 1
        
        l = 0
        len_ans = float('inf')
        ans = ''
        print(hm)
        for r in range(len(s)):
            if s[r] in hm:
                hm[s[r]] -= 1
            if all(v <= 0 for v in hm.values()):
                # print('detect', l, r)
                while all(v <= 0 for v in hm.values()):
                    if s[l] in hm:
                        hm[s[l]] += 1
                    l += 1
                if len_ans >= r - l + 2:
                    ans = s[l - 1: r + 1]
                    len_ans = r - l + 2
                # print(ans, len_ans, l, r, hm)
        
        return ans
            

        


        