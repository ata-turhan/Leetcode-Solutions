class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve_of_eratosthenes(limit: int) -> List[int]:
            # Generate all primes less than or equal to 'limit'
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            primes = [i for i, prime in enumerate(is_prime) if prime]
            return primes

        primes = sieve_of_eratosthenes(1000)  # Since nums[i] <= 1000
        n = len(nums)
        
        prev = 0
        for num in nums:
            # Compute the maximum prime p such that num - p > prev
            max_p = num - prev - 1
            # Find the largest prime less than or equal to max_p
            idx = bisect.bisect_right(primes, max_p) - 1
            if idx >= 0 and primes[idx] < num:
                p = primes[idx]
                num -= p
            # Check if the adjusted num is strictly greater than prev
            if num <= prev:
                return False
            prev = num
        return True