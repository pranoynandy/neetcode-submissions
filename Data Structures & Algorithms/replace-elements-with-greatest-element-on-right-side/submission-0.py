class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        for i in range(len(arr)-1,0,-1):
            if arr[i]>res[-1]:
                res.append(arr[i])
            else:
                res.append(res[-1])

        return res[::-1]

        