class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in numsMap:
                res.append(numsMap[target-nums[i]])
                res.append(i)
                return res
            else:
                numsMap[nums[i]] = i 

        