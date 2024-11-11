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
        for i in range(n):
            adjusted = False
            # Try to subtract the largest possible prime to minimize nums[i]
            for p in reversed(primes):
                if p < nums[i]:
                    x = nums[i] - p
                    if x > prev:
                        nums[i] = x
                        adjusted = True
                        break
            if not adjusted:
                if nums[i] <= prev:
                    return False
                else:
                    prev = nums[i]
            else:
                prev = nums[i]
        return True