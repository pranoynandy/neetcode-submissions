class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0 
        total,res = 0,10001
        while l <= r and r < len(nums):
            total += nums[r]
            while total >= target:
                res = min(res,r-l+1)
                total -= nums[l]
                l+=1
            r+=1
        if res == 10001:
            return 0
        return res
