class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        
        res = []
        for i,j in count.items():
            if j > len(nums)/3:
                res.append(i)

        return res

        