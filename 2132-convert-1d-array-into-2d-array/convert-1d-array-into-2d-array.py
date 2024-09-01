from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if the total number of elements matches the required 2D array dimensions
        if len(original) != m * n:
            return []

        # Initialize the result 2D array
        result = []
        
        # Construct the 2D array by slicing the original array into rows of length 'n'
        for i in range(0, len(original), n):
            result.append(original[i:i+n])

        return result
