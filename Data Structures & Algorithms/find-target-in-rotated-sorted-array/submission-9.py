class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m

            # searching in left portion of array
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1

            #searching in right portion of array
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        
        return -1
            
        