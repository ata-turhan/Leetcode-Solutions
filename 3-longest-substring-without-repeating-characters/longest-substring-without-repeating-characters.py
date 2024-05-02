class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()  # Set to store characters in the current window
        max_len = 0      # Initialize the maximum length of the substring
        left = 0         # Left pointer of the sliding window

        for right, char in enumerate(s):
            # Slide the window to the right until there are no repeating characters
            while char in window:
                window.remove(s[left])
                left += 1

            # Add the current character to the window
            window.add(char)

            # Update the maximum length of the substring
            max_len = max(max_len, right - left + 1)

        return max_len
