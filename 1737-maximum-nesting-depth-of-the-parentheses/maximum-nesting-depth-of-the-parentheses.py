class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0  # Initialize the maximum depth
        cur_depth = 0  # Initialize the current depth
        
        # Iterate through each character in the string
        for char in s:
            if char == "(":  # If the character is an opening parenthesis
                cur_depth += 1  # Increase the current depth
            elif char == ")":  # If the character is a closing parenthesis
                cur_depth -= 1  # Decrease the current depth
            # Update the maximum depth encountered so far
            max_depth = max(max_depth, cur_depth)
        
        return max_depth
