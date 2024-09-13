from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Compute the prefix XOR array
        prefix_xor_array: List[int] = [0]
        cumulative_xor: int = 0
        
        # Build the prefix XOR array
        for num in arr:
            cumulative_xor ^= num
            prefix_xor_array.append(cumulative_xor)

        # Process each query and compute the XOR for the range [start, end]
        result_xor_values: List[int] = []
        for start_index, end_index in queries:
            result_xor_values.append(prefix_xor_array[end_index + 1] ^ prefix_xor_array[start_index])

        return result_xor_values
