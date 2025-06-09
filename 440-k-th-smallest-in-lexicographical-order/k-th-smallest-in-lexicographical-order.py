from typing import List

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Helper function to calculate the number of steps between curr and curr+1
        # in the lexicographical order, within the bounds of n.
        def calculate_steps(prefix1: int, prefix2: int, limit: int) -> int:
            steps: int = 0
            while prefix1 <= limit:
                steps += min(limit + 1, prefix2) - prefix1
                prefix1 *= 10
                prefix2 *= 10
            return steps

        curr: int = 1  # Start from the first number (1)
        k -= 1  # We need to find the (k)-th number but we counted 1 already
                
        # While there are still steps to take
        while k > 0:
            steps: int = calculate_steps(curr, curr + 1, n)
            
            if steps <= k:
                # If the number of steps from curr to curr+1 is less than or equal to k,
                # move to the next number at the same level (curr + 1).
                curr += 1
                k -= steps  # Decrement k by the number of steps we skipped
            else:
                # If the steps exceed k, move downwards to the next level in the lexicographical tree
                # by appending a '0' (i.e., curr *= 10).
                curr *= 10
                k -= 1  # We consumed one step by moving to the next level
        
        return curr
