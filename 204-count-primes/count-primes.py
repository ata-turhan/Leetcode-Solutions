class Solution:
    def countPrimes(self, n: int) -> int:
        # Initialize an array to mark numbers as prime or composite
        is_prime = [True] * n
        # 0 and 1 are not prime
        is_prime[0:2] = [False] * 2
        
        # Iterate through numbers up to the square root of n
        for i in range(2, int(n**0.5)+1):
            # If i is prime, mark its multiples as composite
            if is_prime[i]:
                # Start from i*i and step by i, marking multiples as composite
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # Count the number of primes
        return sum(is_prime)
