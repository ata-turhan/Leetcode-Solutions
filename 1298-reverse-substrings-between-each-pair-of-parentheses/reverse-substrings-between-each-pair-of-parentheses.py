class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                reversed_word = []
                while stack[-1] != "(":
                    reversed_word.append(stack.pop()[::-1])
                stack.pop()
                stack.append("".join(reversed_word))
            else:
                stack.append(char)

        return "".join(stack)