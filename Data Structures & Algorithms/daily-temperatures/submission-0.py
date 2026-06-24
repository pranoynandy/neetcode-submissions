from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp = []
        
        for i,t in enumerate(temperatures):
            while temp and t > temp[-1][1]:
                res[temp[-1][0]] = i-temp[-1][0]
                temp.pop()
            else:
                temp.append([i,t])

        return res
            
            


        