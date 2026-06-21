class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        i=0

        while i in range(len(nums)):
            while 0<i<len(nums)-2 and nums[i-1] == nums[i]:
                i+=1
            l,r = i+1, len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    triplets = [] 
                    triplets.append(nums[i])
                    triplets.append(nums[l])
                    triplets.append(nums[r])
                    res.append(triplets)
                    l+=1
                    r-=1
                    while l<r:
                        if nums[l] == nums[l-1]:
                            l += 1
                        elif nums[r] == nums[r+1]:
                            r -= 1
                        else:
                            break
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else: 
                    r -= 1
            i+=1
        return res
        