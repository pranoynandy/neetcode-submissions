class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        mapS1,mapS2 = [0]*26,[0]*26
        for i in range(len(s1)):
            x = ord(s1[i])-ord('a')
            y = ord(s2[i])-ord('a')
            mapS1[x] = mapS1[x] + 1
            mapS2[y] = mapS2[y] + 1

        l = 0
        for r in range(len(s1), len(s2)):
            if mapS1 == mapS2:
                return True
            x = ord(s2[r])-ord('a')
            y = ord(s2[l])-ord('a')
            mapS2[x] = mapS2[x] + 1
            mapS2[y] = mapS2[y] - 1
            l+=1
            

        return mapS1 == mapS2
        