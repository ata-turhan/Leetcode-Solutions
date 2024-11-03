class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if 'goal' can be obtained by rotating 's'
        # This is true if 'goal' is a substring of 's + s' and both strings have the same length
        return len(goal) == len(s) and goal in (s + s)
