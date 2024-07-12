class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Determine the order of operations based on the values of x and y
        # We prioritize removing the substring that yields the higher points first
        if x >= y:
            first_sub, first_points = "ab", x
            second_sub, second_points = "ba", y
        else:
            first_sub, first_points = "ba", y
            second_sub, second_points = "ab", x
        
        # Helper function to remove substrings and count points
        def remove_and_count(s, sub, points):
            stack = []  # Stack to process the string and remove the specified substring
            total_points = 0  # To keep track of the total points gained
            for char in s:
                # Check if the top of the stack and the current character form the target substring
                if stack and stack[-1] + char == sub:
                    stack.pop()  # Remove the matching character from the stack
                    total_points += points  # Add the points for removing the substring
                else:
                    stack.append(char)  # Otherwise, add the current character to the stack
            # Return the remaining string and the total points gained
            return "".join(stack), total_points
        
        # First pass to remove the prioritized substring and gain points
        remaining_string, points1 = remove_and_count(s, first_sub, first_points)
        
        # Second pass to remove the other substring and gain additional points
        final_string, points2 = remove_and_count(remaining_string, second_sub, second_points)
        
        # Return the total points from both passes
        return points1 + points2
