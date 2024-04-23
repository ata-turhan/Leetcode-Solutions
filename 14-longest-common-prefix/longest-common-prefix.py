class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix among an array of strings.

        Args:
        - strs: A list of strings.

        Returns:
        - The longest common prefix among all strings in strs.
        """
        # Check if the input list is empty
        if not strs:
            return ""

        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            # Iterate over the other strings in strs
            for j in range(1, len(strs)):
                # Check for character mismatches or end of string
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    # Return the longest common prefix found so far
                    return strs[0][:i]
        
        # If no mismatches found, return the entire first string as the prefix
        return strs[0]
