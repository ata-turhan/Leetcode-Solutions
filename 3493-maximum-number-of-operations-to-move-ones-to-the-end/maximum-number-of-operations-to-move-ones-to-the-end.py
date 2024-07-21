class Solution:
    def maxOperations(self, s: str) -> int:
        # Initialize variables to keep track of total moves and current moves
        total_operations = 0
        current_operations = 0
        
        # Iterate through the string from the second last character to the beginning
        for i in range(len(s) - 2, -1, -1):
            # If the current character is '1'
            if s[i] == "1":
                # If the next character is '0'
                if s[i + 1] == "0":
                    # Increment the current operations count
                    current_operations += 1
                # Add current operations count to total operations
                total_operations += current_operations
        
        # Return the total number of operations
        return total_operations
