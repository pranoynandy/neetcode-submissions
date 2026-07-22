class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i,res = 0,[]

        while i in range(len(nums)):
            while 0<i<len(nums)-2 and nums[i-1] == nums[i]:
                i+=1

            l,r = i+1, len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
            i+=1
        return res
        