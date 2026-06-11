class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # if s[0] == ')' or s[0] == ']' or s[0] == '}':
        #     print(s[0])
        #     return False

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif stack != [] and s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif stack != [] and s[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif stack != [] and s[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

        if stack == []:
            return True
        else:
            return False