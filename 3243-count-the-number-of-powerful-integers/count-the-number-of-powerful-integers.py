from functools import lru_cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Calculate the length of s and corresponding multiplier m, tail is int(s)
        k = len(s)
        m = 10 ** k
        tail = int(s)
        
        # If finish is less than tail, no valid x exists.
        if finish < tail:
            return 0
        
        # Calculate valid range for r such that: start <= r * m + tail <= finish.
        if start <= tail:
            r_low = 0
        else:
            # Use ceiling division for (start - tail) / m
            r_low = (start - tail + m - 1) // m
        
        r_high = (finish - tail) // m
        
        # If the lower bound exceeds the upper bound, no powerful integers exist.
        if r_low > r_high:
            return 0
        
        # Helper function: count numbers in [0, n] where every digit is <= limit
        def count_upto(n: int, limit: int) -> int:
            if n < 0:
                return 0
            str_n = str(n)
            L = len(str_n)
            
            @lru_cache(maxsize=None)
            def dp(pos: int, tight: bool, started: bool) -> int:
                if pos == L:
                    # End of the number: if no digit started, number is 0 and counts as 1.
                    return 1
                res = 0
                # Determine the maximum digit we can use at this position.
                # If tight is True, we are bounded by the current digit of n; otherwise, the limit.
                current_bound = int(str_n[pos]) if tight else limit
                # However, we cannot choose a digit greater than limit.
                upper_bound = min(current_bound, limit)
                for dig in range(0, upper_bound + 1):
                    new_tight = tight and (dig == int(str_n[pos]))
                    new_started = started or (dig != 0)
                    res += dp(pos + 1, new_tight, new_started)
                return res
            
            return dp(0, True, False)
        
        # Compute the counts for the range of r's.
        count_high = count_upto(r_high, limit)
        count_low = count_upto(r_low - 1, limit) if r_low > 0 else 0
        
        # The answer is the count of valid r's in [r_low, r_high].
        return count_high - count_low
