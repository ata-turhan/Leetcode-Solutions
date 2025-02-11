class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for char in s:
            stack.append(char)

            while len(stack) >= len(part) and "".join(stack[-len(part):]) == part:
                for _ in range(len(part)):
                    stack.pop()

        return "".join(stack)
        