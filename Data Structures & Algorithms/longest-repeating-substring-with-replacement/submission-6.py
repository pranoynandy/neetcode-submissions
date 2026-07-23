class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count= {}
        result,freq = 0,0
        l,i = 0,0
        while i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i],0)
            freq = max(count.values())
            if i-l+1 - freq <= k:
                result = max(result,i-l+1)
            else:
                count[s[l]]-=1
                l+=1
            i+=1
            
        return result


        