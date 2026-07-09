class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs[0])):
            count = 0
            for j in strs:
                if len(j)-1>=i and strs[0][i] == j[i]:
                    count +=1
                else:
                    return "".join(res)
            if count == len(strs):
                res.append(strs[0][i])
        return "".join(res)

        