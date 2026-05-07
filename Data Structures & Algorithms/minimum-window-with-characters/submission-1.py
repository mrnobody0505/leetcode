class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm = {}
        for c in t:
            hm[c] = hm.get(c, 0) + 1

        need = len(t)   # total chars still needed
        l = 0
        len_ans = float('inf')
        ans = ''

        for r in range(len(s)):
            if s[r] in hm:
                if hm[s[r]] > 0:
                    need -= 1       # one more char satisfied
                hm[s[r]] -= 1

            while need == 0:        # window is valid
                if len_ans > r - l + 1:
                    ans = s[l: r + 1]
                    len_ans = r - l + 1
                if s[l] in hm:
                    hm[s[l]] += 1
                    if hm[s[l]] > 0:
                        need += 1   # lost a needed char
                l += 1

        return ans
                

            


            