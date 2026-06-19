class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0, len(nums)-1
        n = 0
        while n <= j:
            if nums[n] == 0:
                nums[n],nums[i] = nums[i],nums[n]
                i += 1
                n += 1
            elif nums[n] == 1:
                n += 1
            else:
                nums[n],nums[j] = nums[j],nums[n]
                j -= 1

        