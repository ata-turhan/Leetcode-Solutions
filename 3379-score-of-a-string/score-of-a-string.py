class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Calculates the score of the string based on the absolute difference 
        in ASCII values of consecutive characters.
        
        :param s: str - The input string.
        :return: int - The score of the string.
        """
        score = 0  # Initialize the score

        # Iterate over the string from the second character to the end
        for i in range(1, len(s)):
            # Add the absolute difference of ASCII values of consecutive characters to the score
            score += abs(ord(s[i]) - ord(s[i - 1]))

        return score  # Return the calculated score

# Example usage:
# sol = Solution()
# print(sol.scoreOfString("abcd"))  # Output: 3
# print(sol.scoreOfString("az"))    # Output: 25
# print(sol.scoreOfString("abc"))   # Output: 2
