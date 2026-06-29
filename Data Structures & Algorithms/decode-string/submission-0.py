class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                word, num= "",""
                while stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*word)

        result = ''
        while stack:
            result = stack.pop() + result

        return result

        