class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count, star_count, close_count = 0, 0, 0  # Initialize counters for open parentheses, stars, and close parentheses
        
        # Forward pass to check for valid combinations
        for char in s:
            if char == "(":  # If an open parenthesis is encountered
                open_count += 1
            elif char == ")":  # If a close parenthesis is encountered
                close_count += 1
            else:  # If a star is encountered
                star_count += 1
            
            # If the number of close parentheses exceeds the number of open parentheses,
            # adjust the counts accordingly
            if close_count > open_count:
                if star_count == 0:
                    return False
                else:
                    star_count -= 1
                    open_count += 1
        
        open_count, star_count, close_count = 0, 0, 0  # Reset the counts for backward pass
        
        # Backward pass to check for valid combinations
        for char in reversed(s):
            if char == "(":  # If an open parenthesis is encountered
                open_count += 1
            elif char == ")":  # If a close parenthesis is encountered
                close_count += 1
            else:  # If a star is encountered
                star_count += 1
            
            # If the number of open parentheses exceeds the number of close parentheses,
            # adjust the counts accordingly
            if open_count > close_count:
                if star_count == 0:
                    return False
                else:
                    star_count -= 1
                    close_count += 1
        
        return True  # If all combinations are valid, return True
