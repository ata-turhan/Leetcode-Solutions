class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Initialize the length of the previous group and the current group
        prev_length = 0
        curr_length = 1
        total_count = 0

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # If the current character is the same as the previous one, increment the current group length
                curr_length += 1
            else:
                # If the current character is different, count the minimum of the previous and current group lengths
                total_count += min(prev_length, curr_length)
                # Update the previous group length to the current group's length
                prev_length = curr_length
                # Reset the current group length to 1
                curr_length = 1
        
        # Add the count from the last group comparison
        total_count += min(prev_length, curr_length)
        
        return total_count
