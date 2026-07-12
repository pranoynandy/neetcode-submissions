class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs[0])):
            for j in strs:
                if not (len(j)-1>=i and strs[0][i] == j[i]):
                    return "".join(res)                    
            res.append(strs[0][i])
        return "".join(res)

        