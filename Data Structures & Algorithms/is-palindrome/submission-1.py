class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(c.lower() for c in s if c.isalnum())
        print(temp)
        l = 0
        r = len(temp) - 1
        while l < r:
            print(l, temp[l], r, temp[r])
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
        
        return True