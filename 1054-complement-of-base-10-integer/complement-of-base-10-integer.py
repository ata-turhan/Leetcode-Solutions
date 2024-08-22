class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # Calculate the number of bits required to represent 'n'
        num_bits = n.bit_length()
        
        # Create a bitmask with all bits set to 1 of the same length as 'n'
        bitmask = (1 << num_bits) - 1
        
        # The complement of 'n' is the XOR of 'n' with this bitmask
        return bitmask ^ n
