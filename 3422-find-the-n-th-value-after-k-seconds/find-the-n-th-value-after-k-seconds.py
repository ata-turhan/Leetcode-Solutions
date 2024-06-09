class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        values = [1] * n  # Initialize the list with 1's

        for _ in range(k):
            for i in range(1, n):
                values[i] = (values[i] + values[i-1]) % MOD  # Update the current value with the sum of the previous values modulo MOD

        return values[-1] % MOD  # Return the last value in the list modulo MOD
