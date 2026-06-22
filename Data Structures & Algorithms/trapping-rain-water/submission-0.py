class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxL,maxR = height[l],height[r]
        res = 0

        while l<r:
            if maxL>maxR:
                r-=1
                water = min(maxL,maxR)-height[r]
                maxR = max(maxR,height[r])
            else:
                l+=1
                water = min(maxL,maxR)-height[l]
                maxL = max(maxL,height[l])
            if water > 0:
                    res += water

        return res
        