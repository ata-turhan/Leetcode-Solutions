class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Counts unique palindromic subsequences of length 3 in the given string.

        :param s: Input string.
        :return: Number of unique palindromic subsequences of length 3.
        """
        # Dictionary to store the indices of each character in the string
        char_indices = defaultdict(list)
        
        # Populate the dictionary with indices for each character
        for index, char in enumerate(s):
            char_indices[char].append(index)
        
        unique_count = 0

        # Iterate through each character and its indices in the dictionary
        for char, indices in char_indices.items():
            if len(indices) >= 2:  # Only consider characters that appear at least twice
                start = indices[0]  # First occurrence of the character
                end = indices[-1]  # Last occurrence of the character
                
                # Count unique characters between the first and last occurrences
                unique_count += len(set(s[start + 1:end]))
        
        return unique_count
