class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            if len(stack) == 0:
                stack.append([i,heights[i]])
            elif stack[-1][1] < heights[i]:
                stack.append([i,heights[i]])
            elif stack[-1][1] == heights[i]:
                stack.append([i-1,heights[i]])
            else:
                while stack and stack[-1][1] > heights[i]:
                    area = (i-stack[-1][0])*stack[-1][1]
                    maxArea = max(area, maxArea)
                    startIndex = stack[-1][0]
                    stack.pop()
                stack.append([startIndex,heights[i]])
        
        while stack:
            area = (len(heights)-stack[-1][0])*stack[-1][1]
            maxArea = max(area, maxArea)
            stack.pop()

        return maxArea

                



        