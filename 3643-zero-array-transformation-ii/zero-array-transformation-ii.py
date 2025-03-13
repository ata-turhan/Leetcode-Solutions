from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Check if the initial array is already a Zero Array.
        if all(x == 0 for x in nums):
            return 0
        
        n = len(nums)
        m = len(queries)
        
        # Helper function: returns True if the first k queries can reduce nums to a Zero Array.
        def can_zero(k: int) -> bool:
            # Create a difference array of length n+1 (to easily handle range updates)
            diff = [0] * (n)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            curr = 0
            # Compute the prefix sum of diff and check if at every index we have enough decrement.
            for i in range(n):
                curr += diff[i]
                if curr < nums[i]:
                    return False
            return True
        
        # Binary search over the number of queries needed.
        lo, hi = 0, m + 1  # hi is set to m+1 so that hi is an exclusive upper bound.
        ans = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if can_zero(mid):
                ans = mid
                hi = mid  # try to see if we can achieve the result with fewer queries
            else:
                lo = mid + 1
                
        # If no valid k is found within the available queries, return -1.
        if ans == -1 or ans > m:
            return -1
        return ans
