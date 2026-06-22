class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        i,j = 0,0

        while i < len(nums):
            if abs(i-j) <= k:
                if nums[i] in check:
                    return True
                else:
                    check.add(nums[i])
                    i+=1
            else:
                check.remove(nums[j])
                j+=1

        return False