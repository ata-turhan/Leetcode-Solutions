from typing import List
from collections import deque

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # Handle the special case when k is 0
        if k == 0:
            return [0] * len(code)

        n = len(code)
        # Extend the array to simulate circular behavior
        code.extend(code)

        result = []  # Stores the decrypted values

        if k > 0:
            # Compute the initial sum for the first window of size k
            current_window_sum = sum(code[1:k])
            for i in range(k, n + k):
                # Include the current element in the sum
                current_window_sum += code[i]
                result.append(current_window_sum)
                # Remove the leftmost element in the sliding window
                current_window_sum -= code[i - k + 1]
        else:
            # Handle the negative k case
            k = -k
            current_window_sum = sum(code[n - k:n - 1])
            for i in range(n - 1, 2 * n - 1):
                # Include the current element in the sum
                current_window_sum += code[i]
                result.append(current_window_sum)
                # Remove the leftmost element in the sliding window
                current_window_sum -= code[i - k + 1]

        return result
