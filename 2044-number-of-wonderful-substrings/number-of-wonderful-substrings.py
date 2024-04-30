from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Dictionary to store the frequency of each bitmask
        bitmask_freq = defaultdict(int)
        # Initialize the result counter
        result_count = 0
        # Initialize the initial bitmask
        bitmask = 0
        # Initialize the frequency of the zero bitmask
        bitmask_freq[0] = 1

        # Iterate through each character in the word
        for char in word:
            # Calculate the order of the character (0-indexed)
            char_order = ord(char) - ord('a')
            # Update the bitmask by toggling the corresponding bit for the character
            bitmask ^= (1 << char_order)

            # If the current bitmask has been seen before, update the result count
            if bitmask_freq[bitmask] > 0:
                result_count += bitmask_freq[bitmask]
            
            # Increment the frequency of the current bitmask
            bitmask_freq[bitmask] += 1

            # Check for all possible substrings by toggling one bit at a time
            for i in range(10):
                if bitmask_freq[(bitmask ^ (1 << i))] > 0:
                    result_count += bitmask_freq[(bitmask ^ (1 << i))]

        return result_count
