from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Adds one to the given integer represented by an array of digits.

        Args:
        - digits: List of integers representing a non-negative integer

        Returns:
        - List of integers representing the result of adding one to the input number
        """
        # Iterate through the digits in reverse order
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # Increment the current digit by one
            if digits[i] == 10:  # If the digit becomes 10 after incrementing
                digits[i] = 0  # Set the digit to 0
            else:
                break  # Stop the loop if there is no carry-over

        # If the most significant digit becomes 0 after incrementing (indicating a carry-over)
        if digits[0] == 0:
            digits[0] = 1  # Set the most significant digit to 1
            digits.append(0)  # Append a new least significant digit (0)

        return digits  # Return the modified list of digits representing the result
