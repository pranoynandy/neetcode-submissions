class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        total = 0
        res = 10001
        while l < len(nums) and r < len(nums):
            
            total += nums[r]
            #print(nums[l],nums[r],total)
            while total >= target:
                res = min(res,r-l+1)
                print(total)
                total -= nums[l]
                print(nums[l], total)
                l+=1
            r+=1

        if res == 10001:
            return 0

        return res
