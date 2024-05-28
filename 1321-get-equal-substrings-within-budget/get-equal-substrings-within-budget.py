class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        Finds the maximum length of a substring that can be transformed into another substring
        with a given maximum cost.
        
        :param s: str - The original string.
        :param t: str - The target string.
        :param maxCost: int - The maximum cost allowed for transforming the substring.
        :return: int - The maximum length of the transformable substring within the given cost.
        """
        # Calculate the cost difference between corresponding characters in s and t
        diffs = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        
        max_len = 0  # Initialize the maximum length of the substring
        cost = 0  # Initialize the current cost
        left = 0  # Initialize the left pointer of the sliding window
        
        # Iterate over the characters of the strings using the right pointer
        for right in range(len(diffs)):
            cost += diffs[right]  # Add the cost of transforming the current character
            
            # If the current cost exceeds the maximum allowed cost
            while cost > maxCost:
                cost -= diffs[left]  # Remove the cost of the leftmost character
                left += 1  # Move the left pointer to the right
            
            # Update the maximum length of the substring
            max_len = max(max_len, right - left + 1)
        
        return max_len  # Return the maximum length of the transformable substring

# Example usage:
# sol = Solution()
# print(sol.equalSubstring("abcd", "bcdf", 3))  # Output: 3
# print(sol.equalSubstring("abcd", "cdef", 3))  # Output: 1
# print(sol.equalSubstring("abcd", "acde", 0))  # Output: 1
