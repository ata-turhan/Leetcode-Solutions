from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """Finds the pair of closest prime numbers in the given range [left, right]."""
        
        # Step 1: Use Sieve of Eratosthenes to mark prime numbers
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for num in range(2, int(right ** 0.5) + 1):
            if is_prime[num]:
                for multiple in range(num * num, right + 1, num):
                    is_prime[multiple] = False
        
        # Step 2: Find the closest prime pair
        previous_prime, closest_pair = -1, [-1, -1]
        min_difference = float('inf')
        
        for current in range(left, right + 1):
            if is_prime[current]:
                if previous_prime != -1 and (current - previous_prime) < min_difference:
                    min_difference = current - previous_prime
                    closest_pair = [previous_prime, current]
                previous_prime = current  # Update the last seen prime
        
        return closest_pair
