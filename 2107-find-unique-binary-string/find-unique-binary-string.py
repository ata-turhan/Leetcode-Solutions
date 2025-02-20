class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Generates a binary string that is not present in the given list `nums`.
        Uses the Cantor's diagonalization method to guarantee uniqueness.
        """
        unique_binary = []  # Stores the result binary string

        for index, binary_str in enumerate(nums):
            # Flip the diagonal element (i-th character in i-th binary string)
            if binary_str[index] == "0":
                unique_binary.append("1")
            else:
                unique_binary.append("0")

        return "".join(unique_binary)
