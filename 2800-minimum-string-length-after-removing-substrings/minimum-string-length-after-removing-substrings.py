class Solution:
    def minLength(self, s: str) -> int:
        # Convert the string into a list for easy manipulation
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            stack.append(char)
            
            # Check if the last two characters form "AB" or "CD"
            while len(stack) >= 2 and (stack[-2] + stack[-1]) in ("AB", "CD"):
                stack.pop()  # Remove the last character
                stack.pop()  # Remove the second-to-last character

        # The final length of the remaining characters in the stack
        return len(stack)
