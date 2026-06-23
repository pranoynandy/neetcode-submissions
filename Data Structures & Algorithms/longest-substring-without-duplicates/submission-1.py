class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        check = set()
        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[l])
                l+=1
            check.add(s[i])
            res = max(res,i-l+1)

        return res


        