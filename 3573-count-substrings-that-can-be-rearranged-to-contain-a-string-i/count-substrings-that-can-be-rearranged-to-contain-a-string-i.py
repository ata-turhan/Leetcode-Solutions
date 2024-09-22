from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # Count of characters needed from word2
        counts_needed = Counter(word2)
        required = len(counts_needed)  # Number of unique characters needed
        formed = 0  # Number of unique characters that have met their required count

        counts_window = {}  # Count of characters in the current window
        l = 0  # Left pointer of the sliding window
        total_substrings = 0
        N = len(word1)

        for r in range(N):
            # Add the current character to the window
            char_right = word1[r]
            counts_window[char_right] = counts_window.get(char_right, 0) + 1

            # If the current character matches its required count in word2
            if char_right in counts_needed and counts_window[char_right] == counts_needed[char_right]:
                formed += 1

            # Try to shrink the window from the left if it's valid (contains a rearrangement of word2)
            while formed == required:
                # All substrings from current l to r are valid
                total_substrings += N - r

                # Move the left pointer forward to try to find a smaller valid window
                char_left = word1[l]
                counts_window[char_left] -= 1

                if char_left in counts_needed and counts_window[char_left] < counts_needed[char_left]:
                    formed -= 1  # If we lose a required character, decrease the formed count

                l += 1  # Move the left pointer to shrink the window

        return total_substrings
