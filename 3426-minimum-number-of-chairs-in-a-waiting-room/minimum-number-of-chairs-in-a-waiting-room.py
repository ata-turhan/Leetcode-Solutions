class Solution:
    def minimumChairs(self, s: str) -> int:
        """
        Calculates the minimum number of chairs required based on the given string.
        'E' represents an entry and 'L' represents a leave.
        
        :param s: str - The input string consisting of 'E' and 'L'.
        :return: int - The minimum number of chairs required.
        """
        max_chairs_needed = 0  # Initialize the maximum chairs needed
        current_chairs = 0  # Initialize the current chairs in use

        # Iterate over each character in the string
        for char in s:
            if (char == "E"):  # If the character is 'E', increment the current chairs count
                current_chairs += 1
            else:  # If the character is 'L', decrement the current chairs count
                current_chairs -= 1

            # Update the maximum chairs needed
            max_chairs_needed = max(max_chairs_needed, current_chairs)

        return max_chairs_needed  # Return the maximum chairs needed

# Example usage:
# sol = Solution()
# print(sol.minimumChairs("EEEELL"))  # Output: 4
# print(sol.minimumChairs("EELLEE"))  # Output: 2
# print(sol.minimumChairs("EL"))      # Output: 1
