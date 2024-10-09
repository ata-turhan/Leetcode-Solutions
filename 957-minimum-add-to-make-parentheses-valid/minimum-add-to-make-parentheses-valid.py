class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unbalanced_open, unbalanced_close = 0, 0
        for char in s:
            if char == "(":
                unbalanced_open += 1
            else:
                if unbalanced_open > 0:
                    unbalanced_open -= 1
                else:
                    unbalanced_close += 1

        return unbalanced_open + unbalanced_close
        