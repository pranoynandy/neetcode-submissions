class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,i = 0,0
        res = 0
        check = set()
        while i in range(len(s)):
            if s[i] in check:
                check.remove(s[l])
                l+=1
            else:
                check.add(s[i])
                res = max(res,i-l+1)
                i += 1

        return res


        