class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Initialize the result and the mask
        max_xor = 0
        mask = 0
        
        # Iterate through each bit position from the most significant bit to the least significant bit
        for i in range(31, -1, -1):
            mask |= (1 << i)  # Update the mask
            
            prefixes = set()  # Store the prefixes formed by the current bit
            
            # Extract the prefixes formed by the current bit and store them in the set
            for num in nums:
                prefixes.add(num & mask)
            
            # Initialize the potential max XOR with the current max XOR and the bit we're currently checking
            potential_max_xor = max_xor | (1 << i)
            
            # Try to find if there are two prefixes that can XOR to the potential max XOR
            for prefix in prefixes:
                if (prefix ^ potential_max_xor) in prefixes:
                    max_xor = potential_max_xor  # Update the max XOR if found
                    break
        
        return max_xor
