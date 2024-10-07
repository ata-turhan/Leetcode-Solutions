class Solution:
    def minLength(self, s: str) -> int:
        s_arr = list(s)
        stack = []
        for char in s_arr:
            stack.append(char)
            while len(stack) >= 2:
                last_two = stack[-2] + stack[-1]
                if last_two in ("AB", "CD"):
                    stack.pop()
                    stack.pop()
                else:
                    break

        min_str = "".join(stack)
        return len(min_str)
                