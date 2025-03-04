from math import log
from functools import lru_cache

class Solution:
    def checkPowersOfThree(self, target: int) -> bool:
        """Checks if target can be represented as the sum of distinct powers of three."""
        
        @lru_cache(None)
        def can_form_sum(remaining: int) -> bool:
            """Recursively checks if the remaining value can be expressed as a sum of distinct powers of three."""
            if remaining == 0:
                return True
            if remaining < 0:
                return False

            max_power = int(log(remaining, 3))  # Find the highest power of 3 within range
            for exponent in range(max_power, -1, -1):
                if exponent in used_exponents:
                    continue
                used_exponents.add(exponent)
                if can_form_sum(remaining - 3 ** exponent):
                    return True
                used_exponents.remove(exponent)

            return False

        used_exponents = set()
        return can_form_sum(target)
