class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while len(stack) != 0 and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                elif abs(stack[-1]) == abs(a):
                    stack.pop()
                    a = 0
                else:
                    a = 0
            if a != 0:
                stack.append(a)

        return stack