class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                l,r = 0,len(i)-1
                while l<=r:
                    m = l + (r-l)//2
                    if i[m] > target:
                        r = m-1
                    elif i[m] < target:
                        l = m+1
                    else:
                        return True

        return False
        