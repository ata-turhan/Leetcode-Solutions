class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Initialize an array to store the longest ideal string ending at each character
        dp = [0] * 26
        # Initialize the maximum length of the ideal string
        max_length = 0
        # Iterate through each character in the string
        for char in s:
            # Get the index of the current character in the alphabet
            cur_ord = ord(char) - ord('a')
            # Initialize the length of the longest ideal string ending at the current character
            new_val = 1
            # Iterate through all possible characters in the alphabet
            for j in range(26):
                # Check if the absolute difference between the current character and the potential next character
                # is less than or equal to k
                if abs(j - cur_ord) <= k:
                    # Update the length of the longest ideal string ending at the current character
                    new_val = max(new_val, 1 + dp[j])
            # Update the longest ideal string length for the current character
            dp[cur_ord] = new_val
            # Update the maximum length of the ideal string
            max_length = max(max_length, new_val)
        # Return the maximum length of the ideal string
        return max_length
