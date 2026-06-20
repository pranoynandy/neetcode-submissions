class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, count = 0, {0:1}
        total = 0
        for i in nums:
            total += i
            if total - k in count:
                res += count[total-k]
            if total in count:
                count[total] += 1
            else:
                count[total] = 1
        
        return res
        