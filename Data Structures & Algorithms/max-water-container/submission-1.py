class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j =0, len(heights)-1
        res = 0

        while i<j:
            area = min(heights[i],heights[j])*(j-i)
            res = max(area,res)
            if heights[j]>heights[i]: 
                i+=1
            else: 
                j-=1

        return res
            
        