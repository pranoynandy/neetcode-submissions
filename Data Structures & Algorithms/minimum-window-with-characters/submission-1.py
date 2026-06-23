class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        mapT,mapS = {},{}
        for i in t:
            mapT[i] = 1 + mapT.get(i,0)

        have, need = 0, len(mapT)
        res, length = [-1,-1], float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            mapS[c] = 1 + mapS.get(c,0)
            if c in mapT and mapT[c] == mapS[c]:
                have += 1
            while have == need:
                if length > r-l+1:
                    res = [l,r]
                length = min(length,r-l+1)
                mapS[s[l]] -= 1
                if s[l] in mapT and mapS[s[l]] < mapT[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        if length != float("infinity"):
            return s[l:r+1]
        else:
            return ""
        