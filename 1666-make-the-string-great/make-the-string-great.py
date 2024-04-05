class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if stack[-1].lower() != char.lower() or stack[-1] == char:
                    stack.append(char)
                else:
                    stack.pop()
        return "".join(stack)
        