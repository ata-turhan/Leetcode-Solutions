class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize counters for unbalanced open and close parentheses
        unbalanced_open, unbalanced_close = 0, 0
        
        # Iterate through the string
        for char in s:
            if char == "(":
                # Increment unbalanced_open for each open parenthesis
                unbalanced_open += 1
            else:
                # If there's an unbalanced open parenthesis, balance it
                if unbalanced_open > 0:
                    unbalanced_open -= 1
                else:
                    # Otherwise, increment unbalanced_close for each extra close parenthesis
                    unbalanced_close += 1

        # The result is the sum of unbalanced open and close parentheses
        return unbalanced_open + unbalanced_close
