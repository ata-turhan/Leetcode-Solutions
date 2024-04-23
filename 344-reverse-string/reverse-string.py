from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the given list of characters in-place.

        Args:
        - s: List of characters

        Returns:
        - None
        """
        # Iterate through the first half of the list
        for i in range(len(s) // 2):
            # Swap characters at opposite positions
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
