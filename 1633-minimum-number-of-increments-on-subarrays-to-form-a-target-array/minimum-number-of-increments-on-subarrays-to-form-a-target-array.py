from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Initialize previous value to 0 (starting point)
        prev = 0
        # Initialize the number of operations to 0
        operations = 0
        
        # Iterate through each number in the target list
        for num in target:
            # Calculate the difference between the current number and the previous number
            # If the current number is greater than the previous number, add the difference to operations
            # This is because we need to increase all elements from prev to num
            operations += max(0, num - prev)
            # Update the previous number to the current number for the next iteration
            prev = num
        
        return operations
