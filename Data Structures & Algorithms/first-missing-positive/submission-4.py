class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        print(nums)
        
        for i in range(len(nums)):
            x = abs(nums[i])-1
            if 0 <= x < len(nums):
                if nums[x] == 0:
                    nums[x] = -(len(nums)+1)
                elif nums[x] > 0:
                    nums[x] = -(nums[x])
        print(nums)
            
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums)+1

