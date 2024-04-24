from functools import cache

class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        """
        Calculate the nth Tribonacci number using recursion and memoization.

        Args:
        - n: An integer representing the index of the Tribonacci number to calculate.

        Returns:
        - The nth Tribonacci number.
        """
        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            # Recursive calculation with memoization
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
