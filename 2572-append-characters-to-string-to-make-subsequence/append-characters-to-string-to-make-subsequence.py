class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Calculates the minimum number of characters needed to be appended to s
        so that t becomes a subsequence of s.
        
        :param s: str - The input string s.
        :param t: str - The input string t.
        :return: int - The number of characters to append.
        """
        covered = 0  # Initialize the count of characters in t that are covered by s

        # Iterate over each character in s
        for char in s:
            if char == t[covered]:  # If the current character in s matches the current character in t
                covered += 1  # Increment the covered count
                if covered == len(t):  # If all characters in t are covered
                    break  # Exit the loop

        return len(t) - covered  # Return the number of characters left to be appended

# Example usage:
# sol = Solution()
# print(sol.appendCharacters("abc", "ab"))  # Output: 0
# print(sol.appendCharacters("abc", "abcd"))  # Output: 1
# print(sol.appendCharacters("abc", "d"))  # Output: 1
