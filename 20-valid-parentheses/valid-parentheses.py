class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if the given string contains valid parentheses.

        Args:
        - s: The input string containing parentheses.

        Returns:
        - bool: True if the parentheses are valid, False otherwise.
        """
        # Define the mapping of closing to opening parentheses
        paren_mapping = {')': '(', '}': '{', ']': '['}
        # Initialize an empty stack to store opening parentheses
        stack = []
        # Iterate through each character in the string
        for char in s:
            # If the character is an opening parenthesis, push it onto the stack
            if char not in paren_mapping:
                stack.append(char)
            # If the character is a closing parenthesis
            else:
                # Check if the stack is empty (no corresponding opening parenthesis)
                if not stack:
                    return False
                # Check if the opening parenthesis matches the closing parenthesis
                if paren_mapping[char] != stack.pop():
                    return False
        # If the stack is empty, all parentheses have been matched
        return not stack
