class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1,mapS2 = [0]*26,[0]*26
        for i in s1:
            x = ord(i)-ord('a')
            mapS1[x] = mapS1[x] + 1

        l = 0
        for r in range(len(s2)):
            x = ord(s2[r])-ord('a')
            mapS2[x] = mapS2[x] + 1
            if r>=len(s1):
                y = ord(s2[l])-ord('a')
                mapS2[y] = mapS2[y] - 1
                l+=1
            print(mapS2)
            if mapS1 == mapS2:
                return True

        return False
        