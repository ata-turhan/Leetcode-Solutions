class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        Converts the first '6' in the number to a '9' to form the largest possible number.
        """
        digits = list(str(num))

        for i, digit in enumerate(digits):
            if digit == '6':
                digits[i] = '9'
                break  # Only convert the first '6' found

        return int("".join(digits))
