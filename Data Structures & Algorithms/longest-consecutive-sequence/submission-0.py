class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        max_count = 0
        
        for i in nums:
            if i-1 not in x:
                j=i
                count = 0
                while j in x:
                    count += 1
                    max_count = max(max_count, count)
                    j += 1

        return max_count
        