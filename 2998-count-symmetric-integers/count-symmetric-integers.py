class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Counts all symmetric integers between low and high (inclusive).
        A symmetric integer has an even number of digits, and the sum of
        the first half of its digits equals the sum of the second half.
        """
        def is_symmetric(num: int) -> bool:
            digits = str(num)
            n = len(digits)

            if n % 2 != 0:
                return False

            half = n // 2
            return sum(map(int, digits[:half])) == sum(map(int, digits[half:]))

        return sum(1 for num in range(low, high + 1) if is_symmetric(num))
