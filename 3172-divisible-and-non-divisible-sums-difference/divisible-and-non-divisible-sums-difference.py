class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(num if num % m != 0 else -num for num in range(1, n + 1))

        