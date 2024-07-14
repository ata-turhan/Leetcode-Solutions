class Solution:
    def getSmallestString(self, s: str) -> str:
        digits = list(map(int, list(s)))  # Convert the string to a list of integers

        for i in range(len(s) - 1):
            # Check if adjacent digits have the same parity and the current digit is greater than the next
            if digits[i] % 2 == digits[i + 1] % 2 and digits[i] > digits[i + 1]:
                # Swap the digits
                digits[i], digits[i + 1] = digits[i + 1], digits[i]
                break

        return "".join(list(map(str, digits)))  # Convert the list of integers back to a string
