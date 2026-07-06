class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = set()
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
            if count[nums[i]] > len(nums)/3:
                    res.add(nums[i])

        return list(res)

        