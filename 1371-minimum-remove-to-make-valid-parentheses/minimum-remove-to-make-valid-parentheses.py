class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count, close_count = 0, 0  # Initialize counters for open and close parentheses
        stack = []  # Initialize a stack to track parentheses positions
        
        # Iterate through each character in the string
        for char in s:
            stack.append(char)  # Add the current character to the stack
            
            # Update open and close parentheses counts
            if char == "(":
                open_count += 1
            elif char == ")":
                close_count += 1
            
            # If the number of close parentheses exceeds the number of open parentheses,
            # remove the excess close parentheses from the stack
            if close_count > open_count:
                stack.pop()
                close_count -= 1
        
        # If the number of open and close parentheses is equal, return the stack as a string
        if open_count == close_count:
            return "".join(stack)
        else:
            extra_open = open_count - close_count  # Calculate the extra open parentheses
            result = []  # Initialize a list to store the resulting characters
            
            # Iterate through the stack in reverse order
            for i in range(len(stack) - 1, -1, -1):
                # If a closing parenthesis is encountered, reduce the count of extra open parentheses
                if stack[i] == "(":
                    extra_open -= 1
                    # If all extra open parentheses have been matched, add characters to the result list
                    if extra_open == 0:
                        result.extend(stack[:i][::-1])  # Reverse and add characters from the stack
                        break
                else:
                    result.append(stack[i])  # Add non-parentheses characters to the result list
            
            return "".join(result[::-1])  # Reverse and return the result list as a string
