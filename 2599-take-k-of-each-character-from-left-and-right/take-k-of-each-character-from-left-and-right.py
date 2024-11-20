from collections import Counter, defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Edge case: If k is 0, no characters need to be taken
        if k == 0:
            return 0

        # Count the occurrences of each character in the string
        char_count = Counter(s)

        # If any character appears less than k times, it's impossible to satisfy the condition
        if char_count["a"] < k or char_count["b"] < k or char_count["c"] < k:
            return -1

        # Initialize pointers and the sliding window
        right_pointer = len(s)
        window_count = defaultdict(int)
        required_count_met = 0

        # Expand the window from the right to meet the required count for all characters
        while required_count_met < 3:
            right_pointer -= 1
            window_count[s[right_pointer]] += 1
            if window_count[s[right_pointer]] == k:
                required_count_met += 1

        # Calculate the minimum characters needed to satisfy the condition
        min_characters = len(s) - right_pointer

        # Slide the left pointer through the string
        for left_pointer in range(len(s)):
            # Expand the window by including the character at the left pointer
            window_count[s[left_pointer]] += 1

            # Contract the window from the right to maintain valid counts
            while right_pointer < len(s) and window_count[s[right_pointer]] != k:
                window_count[s[right_pointer]] -= 1
                right_pointer += 1

            # Update the minimum characters if a valid window is found
            if left_pointer < right_pointer:
                min_characters = min(min_characters, left_pointer + 1 + len(s) - right_pointer)

        return min_characters
