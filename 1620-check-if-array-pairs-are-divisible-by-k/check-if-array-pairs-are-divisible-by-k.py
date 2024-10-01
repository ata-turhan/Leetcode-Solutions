from collections import Counter
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Count the remainders when dividing the numbers by k
        remainder_count = Counter(num % k for num in arr)
        
        for rem in remainder_count:
            if rem == 0:  # Remainder 0 must have an even count
                if remainder_count[rem] % 2 != 0:
                    return False
            elif 2 * rem == k:  # Special case where remainder is half of k (e.g., k=6, rem=3)
                if remainder_count[rem] % 2 != 0:
                    return False
            else:  # General case: remainder and its complement must have the same count
                if remainder_count[rem] != remainder_count[k - rem]:
                    return False

        return True
