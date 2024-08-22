class Solution:
    def findComplement(self, num: int) -> int:
        # Initialize a variable to track the bitmask of all 1s for the given number
        all_1s = 0
        temp = num

        # Create the bitmask with all bits set to 1 corresponding to the number of bits in num
        while temp > 0:
            temp >>= 1  # Right shift temp to reduce its bits
            all_1s = (all_1s << 1) | 1  # Left shift all_1s and add a 1 to the least significant bit

        # The complement is found by subtracting the original number from the bitmask of all 1s
        return all_1s ^ num  # XOR operation to get the complement
