class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(mid):
            subarray,curSum = 0,0
            for i in nums:
                curSum += i
                if curSum > mid:
                    subarray += 1
                    curSum = i
            return subarray + 1 <= k

        l = max(nums)
        r = sum(nums)
        res = r
        while l<=r:
            m = l + (r-l)//2
            if canSplit(m):
                res = m
                r = m-1
            else:
                l = m+1
        
        return res