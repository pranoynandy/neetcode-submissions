class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        i = 0
        while i in range(len(nums)-3):
            while 0 < i < len(nums)-3 and nums[i] == nums[i-1]:
                i += 1            
            j = i+1
            while j in range(len(nums)-2):
                while 1 < j < len(nums)-2 and nums[j] == nums[j-1]:
                    if (j == i+1):
                        break
                    else:
                        j += 1
                l,r = j+1, len(nums)-1
                while l<r:
                    if nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l,r = l+1, r-1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                j+=1
            i+=1

        return res

        