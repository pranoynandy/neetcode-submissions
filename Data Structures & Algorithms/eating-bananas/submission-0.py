from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        speed = r
        while l<=r:
            m = l+(r-l)//2
            res = 0
            for i in piles:
                res += int(ceil(i/m))
            if res <= h:
                speed = min(m, speed)
                r = m-1
            else:
                l = m+1

        return speed
                
