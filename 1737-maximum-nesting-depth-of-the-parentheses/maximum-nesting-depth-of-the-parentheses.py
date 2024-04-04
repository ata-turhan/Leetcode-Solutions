class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur_depth = 0
        for char in s:
            if char == "(":
                cur_depth += 1
            elif char == ")":
                cur_depth -= 1
            max_depth = max(max_depth, cur_depth)
        return max_depth
        