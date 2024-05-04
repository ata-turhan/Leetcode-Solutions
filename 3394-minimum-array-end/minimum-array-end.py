class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Decrement n since we are considering the array of size n-1
        n -= 1
        
        # Initialize a as x, which will hold the result
        result = x
        
        # Initialize b as 1, representing the rightmost bit position
        bit_position = 1
        
        # Iterate while there are still bits to process in x
        while n > 0:
            # Check if the bit at bit_position is unset in x
            if (bit_position & x) == 0:
                # If unset, set the corresponding bit in result based on the current value of n
                result |= (n & 1) * bit_position
                
                # Right shift n to process the next bit
                n >>= 1
            
            # Left shift bit_position to consider the next bit
            bit_position <<= 1
        
        # Return the final result
        return result
