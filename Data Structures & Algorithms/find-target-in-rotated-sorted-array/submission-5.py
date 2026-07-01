class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m

            # searching in left portion of array
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m-1

            #searching in right portion of array
            else:
                if target < nums[m] or target > nums[r]:
                    r= m-1
                else:
                    l = m+1
        
        return -1
            
        