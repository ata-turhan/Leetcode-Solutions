class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(n):
            # Returns True if n is a prime number, else False
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            # Check for factors from 5 to sqrt(n)
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        special_count = 0
        i = 2
        # Count the number of special numbers in the range [l, r]
        while i * i <= r:
            # Check if i^2 lies within [l, r] and i is prime
            if i * i >= l and is_prime(i):
                special_count += 1
            i += 1

        # Return the total count of numbers in [l, r] minus special numbers
        return (r - l + 1) - special_count