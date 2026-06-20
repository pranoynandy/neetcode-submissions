class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = set(nums)
        i = 1
        while True:
            if i not in check:
                return i
            i+=1