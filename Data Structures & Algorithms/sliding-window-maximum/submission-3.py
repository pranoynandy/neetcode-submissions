from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        dequee = deque()
        for r in range(len(nums)):
            if len(dequee) == 0:
                dequee.append(nums[r])
            else:
                while len(dequee)>0 and dequee[-1] < nums[r]:
                    dequee.pop()
                dequee.append(nums[r])
            
            if r >= k-1:
                res.append(dequee[0])
                if dequee[0] == nums[l]:
                    dequee.popleft()
                l+=1

        return res


        