class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = sum(num for num in range(1, n + 1) if num % m != 0)
        num2 = sum(num for num in range(1, n + 1) if num % m == 0)
        return num1 - num2
        