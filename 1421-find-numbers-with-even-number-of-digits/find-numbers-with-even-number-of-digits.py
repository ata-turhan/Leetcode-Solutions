from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Counts how many numbers in the list have an even number of digits.
        """

        def count_digits(num: int) -> int:
            digits = 0
            while num > 0:
                num //= 10
                digits += 1
            return digits

        even_digit_count = 0
        for num in nums:
            if count_digits(num) % 2 == 0:
                even_digit_count += 1

        return even_digit_count
