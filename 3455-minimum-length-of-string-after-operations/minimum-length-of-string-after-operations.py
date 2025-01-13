class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Calculate the minimum length of the string based on character counts.
        
        :param s: str - Input string.
        :return: int - Minimum length after adjustments.
        """
        # Count occurrences of each character in the string
        char_counts = Counter(s)
        
        # Adjust the counts based on whether they are odd or even
        for char, count in char_counts.items():
            if count % 2 == 1:  # If odd, set count to 1
                char_counts[char] = 1
            else:  # If even, set count to 2
                char_counts[char] = 2
        
        # Return the sum of all adjusted counts as the minimum length
        return sum(char_counts.values())
