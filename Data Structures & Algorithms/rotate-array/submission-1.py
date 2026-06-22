class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k = k%len(nums)
        if k == 0:
            return nums

        def reverse(a,b):
            while a<b:
                nums[a],nums[b] = nums[b],nums[a]
                a+=1
                b-=1

        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)


        #nums = nums[::-1]
        #nums[:] = nums[-k:] + nums[:-k]
        