class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #i,j = 0,0
        res = []
        a = min(len(word1),len(word2))
        for i in range(a):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[i+1::])
        res.append(word2[i+1::])

        print(res)

        return "".join(res)