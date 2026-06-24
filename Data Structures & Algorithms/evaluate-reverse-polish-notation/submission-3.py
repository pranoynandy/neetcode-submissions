class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            
            if i == '+':
                x = stack.pop()
                y = stack.pop()
                res = int(x) + int(y)
                stack.append(res)
            elif i == '-':
                x = stack.pop()
                y = stack.pop()
                res = int(y) - int(x)
                stack.append(res)
            elif i == '*':
                x = stack.pop()
                y = stack.pop()
                res = int(x) * int(y)
                stack.append(res)
            elif i == '/':
                x = stack.pop()
                y = stack.pop()
                res = int(y) / int(x)
                stack.append(res)
            else:
                stack.append(i)

        return int(stack[0])
                

        