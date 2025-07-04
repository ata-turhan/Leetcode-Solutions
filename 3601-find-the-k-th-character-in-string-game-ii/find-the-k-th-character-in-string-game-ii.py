from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        Return the k-th character of the string after applying all operations.
        Operations:
          0 -> append a copy of the current string
          1 -> append the next‐letter transformation of the current string
        """
        n: int = len(operations)
        # lengths[i] = length of word after i operations
        lengths: List[int] = [1] * (n + 1)
        for i in range(1, n + 1):
            lengths[i] = lengths[i - 1] * 2  # each operation doubles the length

        current_k: int = k
        increment_count: int = 0  # total number of +1 shifts to apply

        # Walk operations in reverse to map current_k back to the original 'a'
        for i in range(n, 0, -1):
            prev_len: int = lengths[i - 1]
            if current_k > prev_len:
                # We're in the second half created by the i-th operation
                current_k -= prev_len
                if operations[i - 1] == 1:
                    # A type-1 operation increments each character by 1
                    increment_count += 1
            # else: in the first half, character is unchanged; just continue

        # The base character is 'a'; apply all increments modulo 26
        base_ord: int = ord('a')
        result_ord: int = (base_ord - base_ord + increment_count) % 26 + base_ord
        return chr(result_ord)
