class Solution:
    def toHex(self, num: int) -> str:
        """
        Converts an integer to its hexadecimal representation using two's complement for negative integers.
        
        :param num: int - The input integer.
        :return: str - The hexadecimal representation of the input integer.
        """
        if num == 0:
            return "0"

        # Mapping for hexadecimal characters
        hex_map = "0123456789abcdef"
        result = []

        # Handle two's complement for negative numbers
        if num < 0:
            num += 2 ** 32

        # Convert to hexadecimal
        while num > 0:
            result.append(hex_map[num % 16])
            num //= 16

        return "".join(result[::-1])  # Reverse and join the result list

# Example usage:
# sol = Solution()
# print(sol.toHex(26))  # Output: "1a"
# print(sol.toHex(-1))  # Output: "ffffffff"
