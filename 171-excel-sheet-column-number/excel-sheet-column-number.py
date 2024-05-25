class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Converts a column title as appears in an Excel sheet to its corresponding column number.
        
        :param columnTitle: str - The column title (e.g., "A", "Z", "AA").
        :return: int - The corresponding column number.
        """
        result = 0
        for i, char in enumerate(columnTitle[::-1]):
            # Calculate the value of the character and its position in the title
            result += (ord(char) - ord("A") + 1) * 26 ** i
        return result

# Example usage:
# sol = Solution()
# print(sol.titleToNumber("A"))  # Output: 1
# print(sol.titleToNumber("Z"))  # Output: 26
# print(sol.titleToNumber("AA"))  # Output: 27
# print(sol.titleToNumber("ZY"))  # Output: 701
