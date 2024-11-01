class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for char in s:
            if len(stack) < 2:
                stack.append(char)
            else:
                if char == stack[-1] == stack[-2]:
                    pass
                else:
                    stack.append(char)
        
        return "".join(stack)
        