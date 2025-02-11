class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Removes all occurrences of the substring 'part' from 's' using a stack-based approach.

        :param s: Input string.
        :param part: Substring to be removed.
        :return: Modified string after removing all occurrences of 'part'.
        """
        result_stack = []  # Stack to store characters dynamically

        for char in s:
            result_stack.append(char)  # Add current character to stack

            # Check if the last characters in the stack form the 'part' substring
            if len(result_stack) >= len(part) and "".join(result_stack[-len(part):]) == part:
                for _ in range(len(part)):  
                    result_stack.pop()  # Remove the matched substring

        return "".join(result_stack)  # Convert stack back to string
