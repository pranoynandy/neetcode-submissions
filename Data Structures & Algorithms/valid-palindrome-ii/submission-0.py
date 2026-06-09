class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                skipL, skipR = l+1, r-1
                if (s[skipL:r] == s[r:skipL:-1] or
                    s[l:skipR] == s[skipR:l:-1]):
                    return True
                else:
                    return False
            l+=1
            r-=1
        
        return True
        