class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        file = ""
        for i in path + "/":
            if i == "/":
                if file == "..":
                    if stack: stack.pop()
                elif file != "" and file != ".":
                    stack.append(file)
                file = ""
            else:
                file += i
        
        
        return "/"+"/".join(stack)
        