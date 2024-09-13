from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Compute the prefix XOR array
        prefix_xor: List[int] = [0]
        xor_val: int = 0
        
        # Build the prefix XOR array
        for num in arr:
            xor_val ^= num
            prefix_xor.append(xor_val)

        # Process each query and compute the XOR for the range [start, end]
        result: List[int] = []
        for start, end in queries:
            result.append(prefix_xor[end + 1] ^ prefix_xor[start])

        return result
