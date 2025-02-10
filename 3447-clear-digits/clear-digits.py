class Solution:
    def clearDigits(self, s: str) -> str:
        """
        Removes the character preceding any digit in the given string.
        
        :param s: Input string containing letters and digits.
        :return: Modified string after removing characters preceding digits.
        """
        result_stack = []  # Stack to store non-digit characters

        for char in s:
            if char.isdigit():
                if result_stack:
                    result_stack.pop()  # Remove the last character before the digit
            else:
                result_stack.append(char)  # Add non-digit characters to the stack

        return "".join(result_stack)  # Convert stack back to string
