class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char in "0123456789":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)        