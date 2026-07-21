class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1,1
        #nums.append(1)
        res = [1]
        
        for i in range(len(nums)-1):
            prefix = prefix*nums[i]
            res.append(prefix)

        for i in range(len(nums)-1,0,-1):
            postfix = postfix*nums[i]
            res[i-1] = res[i-1]*postfix
        print(res)

        return res


        