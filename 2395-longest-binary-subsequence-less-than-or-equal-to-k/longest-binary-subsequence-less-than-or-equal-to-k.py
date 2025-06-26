class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Compute the maximum length of a subsequence of binary string `s`
        that, when interpreted as a binary number (allowing leading zeros),
        does not exceed k.
        """
        length: int = 0       # Count of characters included in subsequence
        value: int = 0        # Running numeric value of the subsequence
        bit_pos: int = 0      # Next bit index (0 = LSB, increments for each included bit)

        # Traverse s from end to start: treating end as LSB candidates
        for char in reversed(s):

            if char == '0':
                # Including a '0' never increases `value`,
                # but it consumes one bit-position.
                length += 1
                bit_pos += 1

            else:  # char == '1'
                # The contribution if we include this '1'
                increment = 1 << bit_pos
                # Only include if it keeps us ≤ k
                if value + increment <= k:
                    value += increment
                    length += 1
                    bit_pos += 1
                # Otherwise skip this '1'

        return length
