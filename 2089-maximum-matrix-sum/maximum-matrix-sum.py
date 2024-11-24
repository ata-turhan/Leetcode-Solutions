from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0  # Sum of absolute values of all elements
        min_abs_value = float('inf')  # Minimum absolute value in the matrix
        negative_count = 0  # Count of negative numbers in the matrix

        # Traverse the matrix
        for row in matrix:
            for num in row:
                abs_num = abs(num)
                total_sum += abs_num  # Add absolute value to total_sum
                min_abs_value = min(min_abs_value, abs_num)  # Track the smallest absolute value
                if num < 0:
                    negative_count += 1  # Count negative numbers

        # If the number of negative numbers is even, all can be flipped to positive
        if negative_count % 2 == 0:
            return total_sum
        else:
            # If odd, one negative must remain, so subtract twice the smallest absolute value
            return total_sum - 2 * min_abs_value
