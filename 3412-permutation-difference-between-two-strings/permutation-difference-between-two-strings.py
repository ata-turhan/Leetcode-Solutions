from collections import defaultdict

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # Initialize the result variable to 0
        res = 0
        # Create a defaultdict to store the indices of characters in string s
        indices_s = defaultdict(int)
        # Populate indices_s with the indices of characters in string s
        for i, c in enumerate(s):
            indices_s[c] = i
        # Create a defaultdict to store the indices of characters in string t
        indices_t = defaultdict(int)
        # Populate indices_t with the indices of characters in string t
        for i, c in enumerate(t):
            indices_t[c] = i

        # Iterate over the characters in string s
        for key in indices_s:
            # Add the absolute difference in indices between s and t for each character
            res += abs(indices_s[key] - indices_t[key])

        return res
